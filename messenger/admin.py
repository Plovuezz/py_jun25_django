from django.contrib import admin
from django.contrib.admin import ModelAdmin

from messenger.models import Message


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ("id", "text", "user__username")
    list_select_related = ("user",)
