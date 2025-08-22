from django.urls import path, include

from accounts.views import SignUpView, ActivateAccountView, UserListView, UserListPartialView

app_name = "accounts"

urlpatterns = [
    path("signup", SignUpView.as_view(), name="sign-up"),
    path(
        "activate/<str:uid>/<str:token>/",
        ActivateAccountView.as_view(),
        name="activate",
    ),
    path("", include("django.contrib.auth.urls")),
    path("", UserListView.as_view(), name="user-list"),
    path("patial/", UserListPartialView.as_view(), name="user-list-partial"),
]
