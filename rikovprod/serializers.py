from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'image')


class VideoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'tag', 'embedded_url', 'preview_image', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TagSerializer(serializers.ModelSerializer):
    videos = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Tag
        fields = ['name', 'slug', 'videos']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

