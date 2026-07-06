from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    class Meta:
        abstract = True

class SocialLink(models.Model):
    PLATFORM_CHOICES = [('github', 'GitHub'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('email', 'Email'), ('website', 'Website')]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    url = models.URLField()
    icon = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return f"{self.get_platform_display()}"

class Skill(models.Model):
    CATEGORY_CHOICES = [('backend', 'Backend'), ('frontend', 'Frontend'), ('database', 'Database'), ('tools', 'Tools'), ('other', 'Other')]
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=50)
    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['category', 'order']
    def __str__(self):
        return f"{self.name}"
