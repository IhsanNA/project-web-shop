from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.
def index(request):
    barang = models.barang.objects.all()

    context = {'barangs' : barang}

    return render(request, 'my_app/index.html', context)
