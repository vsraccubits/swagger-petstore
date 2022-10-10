from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "user_status",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        password = make_password(password)
        user = User.objects.create(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.user_status = validated_data.get("user_status", instance.user_status)
        new_password = validated_data.get("password", None)
        if new_password:
            instance.password = make_password(new_password)
        return instance
