from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from main.models import Person, Movie
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils import timezone

class Topic(models.Model):
    title = models.CharField(verbose_name='Tytuł', null=False, blank=False, max_length=250)
    content = models.TextField(verbose_name='Treść', null=False, blank=False, max_length=500)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Topic)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False, max_length=500, verbose_name='Treść')
    date_of_create = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date_of_create']

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False, max_length=500, verbose_name='Treść')
    date_of_create = models.DateTimeField(default=timezone.now)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

