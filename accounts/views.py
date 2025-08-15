from base64 import urlsafe_b64encode

from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db import transaction
from django.shortcuts import render
from django.template.context_processors import request
from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.views import generic

from accounts.forms import CustomUserCreationForm
from accounts.services.token_service import account_activation_token

User = get_user_model()


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/sign_up.html"
    model = User

    @transaction.atomic
    def form_valid(self, form: CustomUserCreationForm):
        # user = form.save(commit=False)
        # user.is_active = False
        # user.save()

        form.instance.is_active = False
        user = form.save()

        mail_subject = "Email confirmation"

        scheme = self.request.scheme
        domain = get_current_site(self.request).domain
        uid = urlsafe_b64encode(force_bytes(user.id))
        token = account_activation_token.make_token(user)

        url = f"{scheme}://{domain}/?uid={uid}&token={token}"

        html_content = render_to_string(
            "registration/emails/acc_active_email.html", {"url": url, "user": user}
        )

        email = EmailMessage(mail_subject, html_content, to=[user.email])
        email.content_subtype = "html"

        email.send()

        return render(self.request, "registration/email_confirmation_sent.html")
