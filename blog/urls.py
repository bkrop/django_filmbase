from os import name
from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostUpdateView, post_comments, comment_replies

urlpatterns = [
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('', PostListView.as_view(), name='home'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('delete_post/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('update_post/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('post_comments/<int:id>', post_comments, name='post_comments'),
    path('comment_replies/<int:comment_id>/', comment_replies, name='comment_replies'),
    # path('post_reply/<int:comment_id>/', post_reply, name='post_reply')
]