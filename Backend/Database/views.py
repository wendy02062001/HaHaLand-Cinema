from django.shortcuts import render
from rest_framework import serializers, status, generics, filters
import Database.models as models
import Database.serializers as serializers
from PIL import Image
from django.http import HttpResponse

# Create your views here.
def secureImage(request, imagePath):
    response = HttpResponse(mimetype="image/jpg")
    img = Image.open(imagePath)
    img.save(response,'jpg')
    return response

class ItemView(generics.ListAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    filterset_fields = ['type']

class ItemCreate(generics.CreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class ItemEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer