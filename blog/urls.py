from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('', PostListView.as_view(), name='home'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('delete_post/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('update_post/<slug:slug>/', PostUpdateView.as_view(), name='post_update')
]