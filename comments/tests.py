from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment


class CommentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            body='Test content',
            author=self.user
        )
        # Get JWT token
        url = reverse('login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_comment(self):
        """Test creating a comment on a post"""
        url = reverse('comment_list_create', kwargs={'post_id': self.post.id})
        data = {
            'body': 'This is a test comment.',
            'post': self.post.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)

    def test_list_comments(self):
        """Test listing comments for a post"""
        Comment.objects.create(
            body='Test comment',
            author=self.user,
            post=self.post
        )
        url = reverse('comment_list_create', kwargs={'post_id': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)