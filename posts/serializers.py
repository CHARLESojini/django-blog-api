from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth.models import User


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        ref_name = 'PostUserMini'  # Add this line



class PostSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    liked_by = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'body', 'cover_photo', 'author',
            'likes_count', 'liked_by', 'comments_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_liked_by(self, obj):
        return [like.user.username for like in obj.likes.all()]

    def get_comments_count(self, obj):
        return obj.comments.count()


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'cover_photo']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
