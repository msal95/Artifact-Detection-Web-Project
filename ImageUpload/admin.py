from django.contrib import admin
from .models import ImageUpload
# Register your models here.

@admin.register(ImageUpload)
class ImageUploadModel(admin.ModelAdmin):
    list_filter = ("id" , "picture", "description")
    list_display = ("id" , "picture", "description")

