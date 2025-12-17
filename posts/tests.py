from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Like


class PostTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Get JWT token
        url = reverse('login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_post(self):
        """Test creating a new post"""
        url = reverse('post_list_create')
        data = {
            'title': 'Test Post',
            'body': 'This is a test post content.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_list_posts(self):
        """Test listing all posts"""
        Post.objects.create(
            title='Test Post',
            body='Test content',
            author=self.user
        )
        url = reverse('post_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_post(self):
        """Test liking a post"""
        post = Post.objects.create(
            title='Test Post',
            body='Test content',
            author=self.user
        )
        url = reverse('like_post', kwargs={'pk': post.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        """Test unliking a post"""
        post = Post.objects.create(
            title='Test Post',
            body='Test content',
            author=self.user
        )
        Like.objects.create(user=self.user, post=post)
        url = reverse('like_post', kwargs={'pk': post.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.count(), 0)