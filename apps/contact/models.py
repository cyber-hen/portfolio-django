from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from apps.core.models import TimeStampedModel

class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)
    reply_message = models.TextField(blank=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.subject}"
    def send_confirmation(self):
        subject = f'We received your message - {self.subject}'
        message = f"Hello {self.name},\n\nThank you for reaching out. We've received your message and will get back to you soon.\n\nBest regards,\nPortfolio Team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email], fail_silently=False)
    def send_reply(self):
        subject = f'Re: {self.subject}'
        send_mail(subject, self.reply_message, settings.DEFAULT_FROM_EMAIL, [self.email], fail_silently=False)
