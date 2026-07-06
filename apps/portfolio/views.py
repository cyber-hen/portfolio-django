from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category, Project, ProjectImage
from .serializers import CategorySerializer, ProjectListSerializer, ProjectDetailSerializer, ProjectImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'description', 'technologies']
    ordering_fields = ['created_at', 'view_count', 'order']
    ordering = ['-featured', 'order', '-created_at']
    lookup_field = 'slug'
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectListSerializer
    @action(detail=True, methods=['post'])
    def increment_views(self, request, slug=None):
        project = self.get_object()
        project.view_count += 1
        project.save()
        serializer = self.get_serializer(project)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def featured(self, request):
        projects = Project.objects.filter(featured=True)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def recent(self, request):
        projects = Project.objects.all()[:6]
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['project']
