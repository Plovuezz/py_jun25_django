from django.urls import path, include

from accounts.views import SignUpView

app_name = "accounts"

urlpatterns = [
    path("signup", SignUpView.as_view(), name="sign-up"),
    path("", include("django.contrib.auth.urls")),
]
