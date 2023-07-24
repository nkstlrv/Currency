from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView, FormView
from django.urls import reverse_lazy
from .forms import PasswordResetForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
    

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Successful password change')
        return response
