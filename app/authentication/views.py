from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class ProgileView(UpdateView):
    model = get_user_model()
    template_name = 'authentication/profile_view.html'
    success_url = reverse_lazy('profile')
    fields = (
        'first_name',
        'last_name',
        'email',
        'username'
    )