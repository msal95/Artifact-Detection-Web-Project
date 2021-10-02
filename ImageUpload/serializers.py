from rest_framework import serializers
from .models import ImageUpload

# Driver Serializer
class ImageUploadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ImageUpload
        fields = "__all__"


