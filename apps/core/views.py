from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import SocialLink, Skill
from .serializers import SocialLinkSerializer, SkillSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        skills = Skill.objects.all()
        data = {}
        for skill in skills:
            category = skill.get_category_display()
            if category not in data:
                data[category] = []
            data[category].append(SkillSerializer(skill).data)
        return Response(data)
