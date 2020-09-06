from django.contrib import admin
from .models import Comment, Topic, Reply

admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(Reply)