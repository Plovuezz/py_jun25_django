from django.urls import path

from messenger.views import HomeView, MessageListView, message_detail_view

app_name = "messenger"

urlpatterns = [
    path(
        "home/",
        HomeView.as_view(),
        name="home"
    ),
    path(
        "messages/",
        MessageListView.as_view(),
        name="message-list"
    ),
    path(
        "messages/<int:pk>/",
        message_detail_view,
        name="message-detail"
    )
]
