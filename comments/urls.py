from django.urls import path
from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('post/<int:post_id>/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
]