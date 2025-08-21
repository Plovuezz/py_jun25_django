from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(
        null=True, blank=True, upload_to="accounts/profiles/avatars/"
    )
    bio = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
