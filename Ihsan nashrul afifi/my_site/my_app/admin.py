from django.contrib import admin
from . models import barang

# Register your models here.

class barangAdmin(admin.ModelAdmin):
    list_display = ['nama','gambar']
    search_fields = ['nama',]

admin.site.register(barang, barangAdmin)
