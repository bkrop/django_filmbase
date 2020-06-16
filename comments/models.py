from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False, max_length=500)
    date_of_create = models.DateField(auto_now=True, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)