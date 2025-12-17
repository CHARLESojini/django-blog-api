from django.urls import path
from .views import PostListCreateView, PostDetailView, LikePostView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
]