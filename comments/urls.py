from django.urls import path
from .views import TopicCreateView, TopicDetailView

urlpatterns = [
    path('<slug:slug>/', TopicCreateView.as_view(), name='create_topic'),
    path('<slug:slug>/<slug:topic_slug>/', TopicDetailView.as_view(), name='detail_topic')#film/topic
]