from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class PhotoAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class VideoAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerialiazer
    lookup_field = 'slug'


class TagAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
