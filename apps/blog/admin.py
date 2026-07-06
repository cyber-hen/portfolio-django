from django.contrib import admin
from .models import BlogCategory, BlogPost

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published', 'featured', 'view_count']
    list_filter = ['category', 'published', 'featured', 'created_at']
    list_editable = ['published', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    readonly_fields = ['view_count', 'created_at', 'updated_at']
