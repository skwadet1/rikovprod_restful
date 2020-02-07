from django.db import models
from autoslug import AutoSlugField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, default='Video')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return 'Tag N: {id}, name: {text}'.format(id=self.id, text=self.name)


class Video(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = AutoSlugField(populate_from='title')
    tag = models.ManyToManyField(Tag, related_name='videos')
    embedded_url = models.URLField(max_length=200)
    preview_image = models.FileField(upload_to='previews/')

    def __str__(self):
        return 'Video N: {id}, title: {title}'.format(id=self.id, title=self.title)


class Photo(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    image = models.FileField(upload_to='photos/')

    def __str__(self):
        return 'Photo N: {id}, title: {title}'.format(id=self.id, title=self.title)
