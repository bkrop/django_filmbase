from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200)
    content = models.TextField(null=False, blank=False, max_length=1000)
    date_of_create = models.DateField(null=False, blank=False, auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)