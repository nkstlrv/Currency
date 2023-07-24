from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView, FormView
from django.urls import reverse_lazy
from .forms import PasswordResetForm
from django.contrib import messages


class ProgileView(UpdateView):
    model = get_user_model()
    template_name = 'authentication/profile_view.html'
    success_url = reverse_lazy('home')
    fields = (
        'first_name',
        'last_name',
        'email',
        'username',
        'is_superuser', # This is temporary field; will be removed when registration will be availale
    
    )   


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successful password reset")
        return super().form_valid(form)
    