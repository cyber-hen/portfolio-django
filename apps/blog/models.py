from django.db import models
from django.contrib.auth.models import User
from django.utils.slug import slugify
from apps.core.models import TimeStampedModel

class BlogCategory(models.Model):
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

class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name='posts')
    featured_image = models.ImageField(upload_to='blog/%Y/%m/%d/')
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    read_time = models.IntegerField(default=5)
    tags = models.CharField(max_length=500, blank=True)
    class Meta:
        ordering = ['-published', '-created_at']
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    @property
    def tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
