from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import ContactMessage
from .serializers import ContactMessageSerializer, ContactMessageDetailSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['read', 'replied']
    search_fields = ['name', 'email', 'subject']
    ordering_fields = ['created_at', 'read']
    ordering = ['-created_at']
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ContactMessageDetailSerializer
        return ContactMessageSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        try:
            contact = serializer.instance
            contact.send_confirmation()
        except Exception as e:
            print(f"Error sending confirmation email: {e}")
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Message sent successfully!'}, status=status.HTTP_201_CREATED, headers=headers)
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def send_reply(self, request, pk=None):
        contact = self.get_object()
        reply_message = request.data.get('reply_message')
        if not reply_message:
            return Response({'error': 'reply_message is required'}, status=status.HTTP_400_BAD_REQUEST)
        contact.reply_message = reply_message
        contact.replied = True
        contact.save()
        try:
            contact.send_reply()
        except Exception as e:
            print(f"Error sending reply email: {e}")
        serializer = self.get_serializer(contact)
        return Response(serializer.data)
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def mark_as_read(self, request, pk=None):
        contact = self.get_object()
        contact.read = True
        contact.save()
        serializer = self.get_serializer(contact)
        return Response(serializer.data)
