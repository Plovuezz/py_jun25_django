from django.conf import settings
from django.db import models
from django.urls import reverse


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return self.text

    def get_absolute_url(self):
        return reverse("messenger:message-detail", args=(self.id,))
