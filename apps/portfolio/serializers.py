from rest_framework import serializers
from .models import Category, Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption', 'order']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class ProjectListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'short_description', 'image', 'category', 'category_name', 'technologies', 'featured', 'view_count', 'created_at']

class ProjectDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    technologies_list = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'short_description', 'image', 'featured_image', 'category', 'category_name', 'technologies', 'technologies_list', 'github_link', 'live_link', 'featured', 'view_count', 'created_at', 'updated_at', 'images']
    def get_technologies_list(self, obj):
        return [tech.strip() for tech in obj.technologies.split(',')]
