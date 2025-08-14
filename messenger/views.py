from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "messenger/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        num_messages = Message.objects.count()
        context["num_messages"] = num_messages

        if last_viewed_message_id := self.request.session.get("last_viewed_message_id"):
            try:
                context["last_viewed_message"] = Message.objects.get(
                    pk=last_viewed_message_id
                )
            except Message.DoesNotExist:
                del self.request.session["last_viewed_message_id"]

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


# def message_detail_view(
#         request: HttpRequest,
#         pk: int
# ) -> HttpResponse:
#     message = get_object_or_404(Message, pk=pk)
#
#     context = {
#         "message": message
#     }
#
#     return render(
#         request,
#         "messenger/message_detail.html",
#         context
#     )


class MessageDetailView(generic.DetailView):
    model = Message

    def get_object(self, *args, **kwargs):
        message = super().get_object(*args, **kwargs)

        self.request.session["last_viewed_message_id"] = message.id

        return message


def message_create_view(request):
    if request.method == "GET":
        return render(request, "messenger/message_form.html")

    if request.method == "POST":
        text = request.POST["text"]
        Message.objects.create(text=text, user=request.user)

        return HttpResponseRedirect(
            reverse("messenger:message-list")
        )
