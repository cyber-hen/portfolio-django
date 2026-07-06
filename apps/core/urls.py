from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialLinkViewSet, SkillViewSet
router = DefaultRouter()
router.register(r'social-links', SocialLinkViewSet, basename='sociallink')
router.register(r'skills', SkillViewSet, basename='skill')
urlpatterns = [path('', include(router.urls))]
