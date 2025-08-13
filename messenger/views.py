from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import generic

from messenger.models import Message


# def home(request: HttpRequest) -> HttpResponse:
#     num_messages = Message.objects.count()
#
#     context = {
#         "num_messages": num_messages
#     }
#
#     return render(
#         request,
#         "messenger/home.html",
#         context
#     )

class HomeView(generic.TemplateView):
    template_name = "messenger/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        num_messages = Message.objects.count()
        context["num_messages"] = num_messages
        context["last_viewed_message"] = self.request.session.get("last_viewed_message")

        return context


# def message_list_view(request: HttpRequest) -> HttpResponse:
#     message_list = Message.objects.all()
#
#     return render(
#         request,
#         "messenger/message_list.html",
#         {"message_list": message_list}
#     )


class MessageListView(generic.ListView):
    model = Message


def message_detail_view(
        request: HttpRequest,
        pk: int
) -> HttpResponse:
    message = get_object_or_404(Message, pk=pk)

    context = {
        "message": message
    }

    return render(
        request,
        "messenger/message_detail.html",
        context
    )


class MessageDetailView(generic.DetailView):
    model = Message
