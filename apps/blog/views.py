from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import BlogCategory, BlogPost
from .serializers import BlogCategorySerializer, BlogPostListSerializer, BlogPostDetailSerializer

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(published=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author', 'featured']
    search_fields = ['title', 'content', 'tags']
    ordering_fields = ['created_at', 'view_count']
    ordering = ['-created_at']
    lookup_field = 'slug'
    def get_queryset(self):
        if self.request.user.is_staff:
            return BlogPost.objects.all()
        return BlogPost.objects.filter(published=True)
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        return BlogPostListSerializer
    @action(detail=True, methods=['post'])
    def increment_views(self, request, slug=None):
        post = self.get_object()
        post.view_count += 1
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def featured(self, request):
        posts = self.get_queryset().filter(featured=True)[:3]
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def recent(self, request):
        posts = self.get_queryset()[:6]
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
