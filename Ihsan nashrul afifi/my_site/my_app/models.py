from django.db import models

# Create your models here.

class barang(models.Model):

    nama = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
