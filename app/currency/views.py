from django.http import JsonResponse
from currency import models
from currency.forms import ContactsForm, RatesForm, SourcesForm
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeTemplateView(TemplateView):
    template_name = "currency/index.html"


class RatesListView(ListView):
    model = models.Rate
    context_object_name = "rates"
    template_name = "currency/rates.html"


class RateCreateView(CreateView, LoginRequiredMixin):
    model = models.Rate
    form_class = RatesForm
    template_name = "currency/rate_create.html"
    success_url = reverse_lazy("rates_table")


class RateUpdateView(UpdateView, LoginRequiredMixin):
    model = models.Rate
    form_class = RatesForm
    template_name = "currency/rate_update.html"
    success_url = reverse_lazy("rates_table")


class RateDeleteView(DeleteView, LoginRequiredMixin):
    model = models.Rate
    template_name = "currency/rate_delete.html"
    success_url = reverse_lazy("rates_table")


class ContactsListView(ListView):
    model = models.ContactUs
    context_object_name = "contacts"
    template_name = "currency/contacts.html"


class ContactCreateView(CreateView, LoginRequiredMixin):
    model = models.ContactUs
    form_class = ContactsForm
    template_name = "currency/contact_create.html"
    success_url = reverse_lazy("contacts_table")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data

        email_body = f"""
        From: {cleaned_data['email_from']}
        Subject: {cleaned_data['subject']}
        Message: {cleaned_data['message']}
        """

        from django.conf import settings

        send_mail(
            "Contact Us",
            email_body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return super().form_valid(form)


class ContactUpdateView(UpdateView, LoginRequiredMixin):
    model = models.ContactUs
    form_class = ContactsForm
    template_name = "currency/contact_update.html"
    success_url = reverse_lazy("contacts_table")


class ContactDeleteView(DeleteView, LoginRequiredMixin):
    model = models.ContactUs
    template_name = "currency/contact_delete.html"
    success_url = reverse_lazy("contacts_table")


class SourcesListView(ListView):
    model = models.Source
    context_object_name = "sources"
    template_name = "currency/sources.html"


class SourceCreateView(CreateView, LoginRequiredMixin):
    model = models.Source
    form_class = SourcesForm
    template_name = "currency/source_create.html"
    success_url = reverse_lazy("sources_table")


class SourceUpdateView(UpdateView, LoginRequiredMixin):
    model = models.Source
    form_class = SourcesForm
    template_name = "currency/source_update.html"
    success_url = reverse_lazy("sources_table")


class SourceDeleteView(DeleteView, LoginRequiredMixin):
    model = models.Source
    template_name = "currency/source_delete.html"
    success_url = reverse_lazy("sources_table")


class MiddlewareLogListView(ListView, LoginRequiredMixin):
    model = models.RequestResponseLog
    context_object_name = "logs"
    template_name = "currency/middlewarelogs.html"


def rates_json(request):
    data = {}

    rates = models.Rate.objects.all()
    if rates:
        for ind, rate in enumerate(rates, start=1):
            data[ind] = {
                "id": rate.id,
                "currency": rate.currency,
                "buy": rate.buy,
                "sell": rate.sell,
                "source": rate.source,
                "created": rate.created,
            }

    return JsonResponse(data)


def contacts_json(request):
    data = {}

    contacts = models.ContactUs.objects.all()
    if contacts:
        for ind, contact in enumerate(contacts, start=1):
            data[ind] = {
                "id": contact.id,
                "email_from": contact.email_from,
                "subject": contact.subject,
                "message": contact.message,
            }

    return JsonResponse(data)
