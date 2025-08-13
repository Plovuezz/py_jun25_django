from django.urls import path

from messenger.views import HomeView, MessageListView, MessageDetailView

app_name = "messenger"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("messages/", MessageListView.as_view(), name="message-list"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
]
