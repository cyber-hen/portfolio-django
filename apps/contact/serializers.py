from rest_framework import serializers
from .models import ContactMessage

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']

class ContactMessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'phone', 'read', 'replied', 'reply_message', 'created_at']
        read_only_fields = ['id', 'created_at']
