from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from main.models import Person, Movie

class Topic(models.Model):
    title = models.CharField(verbose_name='Tytuł', null=False, blank=False, max_length=250)
    content = models.TextField(verbose_name='Treść', null=False, blank=False, max_length=500)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False, max_length=500)
    date_of_create = models.DateField(auto_now=True, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)