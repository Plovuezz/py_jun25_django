from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile


class ProfileInline(admin.TabularInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileInline]
