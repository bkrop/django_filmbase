from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail')
]