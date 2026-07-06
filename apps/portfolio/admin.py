from django.contrib import admin
from .models import Category, Project, ProjectImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'view_count']
    list_filter = ['category', 'featured', 'created_at']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']
    inlines = [ProjectImageInline]
    readonly_fields = ['view_count', 'created_at', 'updated_at']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    list_filter = ['project']
