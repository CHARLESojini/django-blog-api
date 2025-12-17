from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'post', 'created_at']
        read_only_fields = ['author', 'created_at']
        ref_name = 'CommentUserMini'  # Add this line


    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)