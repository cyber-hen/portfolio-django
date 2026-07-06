from django.db import models
from django.utils.slug import slugify
from apps.core.models import TimeStampedModel

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Project(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    featured_image = models.ImageField(upload_to='projects/featured/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    technologies = models.CharField(max_length=500)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    view_count = models.IntegerField(default=0)
    class Meta:
        ordering = ['-featured', 'order', '-created_at']
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/%Y/%m/%d/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return f"{self.project.title}"
