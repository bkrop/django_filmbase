from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django_filmbase.utils import unique_slug_generator
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200)
    content = models.TextField(null=False, blank=False, max_length=1000)
    date_of_create = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'

    def get_class(self):
        return self.__class__.__name__

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)

