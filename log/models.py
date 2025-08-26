from django.db import models


class RequestLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=15)
    path = models.CharField(max_length=128)
    username = models.CharField(max_length=128, blank=True)
    status_code = models.IntegerField()
