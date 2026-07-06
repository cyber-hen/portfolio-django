from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'replied', 'created_at']
    list_filter = ['read', 'replied', 'created_at']
    list_editable = ['read', 'replied']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at', 'updated_at']
