from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    picture = models.ImageField(upload_to="static/"  ,blank = True)
    description = models.CharField(max_length=5000, default = "")
    