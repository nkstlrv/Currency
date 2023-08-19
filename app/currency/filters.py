import django_filters
from .models import Rate, Source, ContactUs, RequestResponseLog


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = ("source", "currency")


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ("url", "name")


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = ("email_from", "subject")
