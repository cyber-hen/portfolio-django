from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogCategory, BlogPost

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug', 'description']

class BlogPostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'excerpt', 'featured_image', 'author', 'category', 'category_name', 'published', 'featured', 'view_count', 'read_time', 'created_at']

class BlogPostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    tags_list = serializers.SerializerMethodField()
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'featured_image', 'author', 'category', 'category_name', 'published', 'featured', 'view_count', 'read_time', 'tags', 'tags_list', 'created_at', 'updated_at']
    def get_tags_list(self, obj):
        return obj.tags_list
