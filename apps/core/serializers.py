from rest_framework import serializers
from .models import SocialLink, Skill

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'url', 'icon', 'order']

class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_display', 'proficiency', 'icon', 'order']
