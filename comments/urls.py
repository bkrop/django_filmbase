from django.urls import path
from .views import TopicCreateView

urlpatterns = [
    path('<slug:slug>/', TopicCreateView.as_view(), name='create_topic')
]