from django.http import JsonResponse
from currency import models
from currency.forms import ContactsForm, RatesForm, SourcesForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


class HomeTemplateView(TemplateView):
    template_name = 'currency/index.html'


class RatesListView(ListView):
    model = models.Rate
    context_object_name = 'rates'
    template_name = 'currency/rates.html'


class RateCreateView(CreateView):
    model = models.Rate
    form_class = RatesForm
    template_name = 'currency/rate_create.html'
    success_url = reverse_lazy('rates_table')


class RateUpdateView(UpdateView):
    model = models.Rate
    form_class = RatesForm
    template_name = 'currency/rate_update.html'
    success_url = reverse_lazy('rates_table')


class RateDeleteView(DeleteView):
    model = models.Rate
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('rates_table')


class ContactsListView(ListView):
    model = models.ContactUs
    context_object_name = 'contacts'
    template_name = 'currency/contacts.html'


class ContactCreateView(CreateView):
    model = models.ContactUs
    form_class = ContactsForm
    template_name = 'currency/contact_create.html'
    success_url = reverse_lazy('contacts_table')


class ContactUpdateView(UpdateView):
    model = models.ContactUs
    form_class = ContactsForm
    template_name = 'currency/contact_update.html'
    success_url = reverse_lazy('contacts_table')


class ContactDeleteView(DeleteView):
    model = models.ContactUs
    template_name = 'currency/contact_delete.html'
    success_url = reverse_lazy('contacts_table')


class SourcesListView(ListView):
    model = models.Source
    context_object_name = 'sources'
    template_name = 'currency/sources.html'


class SourceCreateView(CreateView):
    model = models.Source
    form_class = SourcesForm
    template_name = 'currency/source_create.html'
    success_url = reverse_lazy('sources_table')


class SourceUpdateView(UpdateView):
    model = models.Source
    form_class = SourcesForm
    template_name = 'currency/source_update.html'
    success_url = reverse_lazy('sources_table')


class SourceDeleteView(DeleteView):
    model = models.Source
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('sources_table')


def rates_json(request):
    data = {}

    rates = models.Rate.objects.all()
    if rates:
        for ind, rate in enumerate(rates, start=1):
            data[ind] = {
                'id': rate.id,
                'currency': rate.currency,
                'buy': rate.buy,
                'sell': rate.sell,
                'source': rate.source,
                'created': rate.created
            }

    return JsonResponse(data)


def contacts_json(request):
    data = {}

    contacts = models.ContactUs.objects.all()
    if contacts:
        for ind, contact in enumerate(contacts, start=1):
            data[ind] = {
                'id': contact.id,
                'email_from': contact.email_from,
                'subject': contact.subject,
                'message': contact.message
            }

    return JsonResponse(data)
