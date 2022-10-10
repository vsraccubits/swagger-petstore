from django.contrib import admin

from pets.models import Category, Pet, PhotoUrl, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "status")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(PhotoUrl)
