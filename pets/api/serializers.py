from rest_framework import serializers

from pets import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class PhotoUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoUrl
        fields = "__all__"


class PetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    photo_urls = PhotoUrlsSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Pet
        fields = "__all__"

    def create(self, validated_data):
        category = validated_data.pop("category")
        tags = validated_data.pop("tags")
        category_obj = models.Category.objects.create(**category)
        pet = models.Pet.objects.create(category=category_obj, **validated_data)
        for tag in tags:
            tag_obj = models.Tag.objects.create(**tag)
            pet.tags.add(tag_obj)
        return pet

    def update(self, instance, validated_data):
        category_data = validated_data.pop("category")
        category = instance.category

        tags_data = validated_data.pop("tags")
        for tag in instance.tags.all():
            tag.delete()
        for tag_data in tags_data:
            tag_obj = models.Tag.objects.create(**tag_data)
            instance.tags.add(tag_obj)

        instance.name = validated_data.get("name", instance.name)
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        category.name = category_data.get("name", category.name)
        category.save()

        return instance
