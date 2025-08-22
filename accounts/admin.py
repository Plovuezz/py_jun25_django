from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj):
        return False


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileInline]
