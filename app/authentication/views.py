from django.contrib.auth import get_user_model
from django.views.generic import UpdateView, FormView, CreateView, RedirectView
from django.urls import reverse_lazy
from .forms import PasswordResetForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProgileView(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    template_name = "authentication/profile_view.html"
    success_url = reverse_lazy("home")
    fields = (
        "first_name",
        "last_name",
        "email",
        # This is temporary field; will be removed when registration will be availale
        "is_superuser",
    )


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = "authentication/password_reset.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successful password reset")
        return super().form_valid(form)


class PasswordChangeView(PasswordChangeView, LoginRequiredMixin):
    form_class = PasswordChangeForm
    template_name = "authentication/password_change.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Successful password change")
        return response


class SignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = SignUpForm


class UserActivateView(RedirectView):
    pattern_name = "login"

    def get_redirect_url(self, *args, **kwargs):
        username = str(kwargs.pop("username"))
        user = get_user_model().objects.filter(username=username).only("id").first()

        if user is not None:
            user.is_active = True
            user.save(update_fields=["is_active"])

        return super().get_redirect_url(*args, **kwargs)
