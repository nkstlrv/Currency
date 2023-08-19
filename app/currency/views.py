from currency import models
from currency.forms import ContactsForm, RatesForm, SourcesForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import send_email_contact_us
from django_filters.views import FilterView
from .filters import RateFilter, SourceFilter, ContactUsFilter

# import re


class HomeTemplateView(TemplateView):
    template_name = "currency/index.html"

    # Added instant redirection to rates table page
    def get(self, request, *args, **kwargs):
        return redirect("rates_table")


class RatesListView(FilterView):
    queryset = models.Rate.objects.all().order_by("-id").select_related("source")
    context_object_name = "rates"
    template_name = "currency/rates.html"
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context["filter_params"] = "&".join(
            f"{key}={value}" for key, value in self.request.GET.items() if key != "page"
        )
        # context["filter_params"] = re.sub(
        #     r"(\?|&)page=(\d*)&*", "", string=self.request.GET.urlencode()
        # )

        return context


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


class ContactsListView(FilterView):
    model = models.ContactUs
    context_object_name = "contacts"
    template_name = "currency/contacts.html"
    paginate_by = 10
    filterset_class = ContactUsFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context["filter_params"] = "&".join(
            f"{key}={value}" for key, value in self.request.GET.items() if key != "page"
        )
        # context["filter_params"] = re.sub(
        #     r"(\?|&)page=(\d*)&*", "", string=self.request.GET.urlencode()
        # )

        return context


class ContactCreateView(CreateView, LoginRequiredMixin):
    model = models.ContactUs
    form_class = ContactsForm
    template_name = "currency/contact_create.html"
    success_url = reverse_lazy("contacts_table")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data

        # Sending email to Customer support
        send_email_contact_us.delay(cleaned_data)
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


class SourcesListView(FilterView):
    # model = models.Source
    queryset = models.Source.objects.all().order_by("id")
    context_object_name = "sources"
    template_name = "currency/sources.html"
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context["filter_params"] = "&".join(
            f"{key}={value}" for key, value in self.request.GET.items() if key != "page"
        )
        # context["filter_params"] = re.sub(
        #     r"(\?|&)page=(\d*)&*", "", string=self.request.GET.urlencode()
        # )

        return context


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
    queryset = models.RequestResponseLog.objects.all().order_by("-id")
    context_object_name = "logs"
    template_name = "currency/middlewarelogs.html"
    paginate_by = 10
