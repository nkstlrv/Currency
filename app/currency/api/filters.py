from django_filters import FilterSet
from currency.models import Rate, Source, ContactUs, RequestResponseLog


class RateFilter(FilterSet):
    class Meta:
        model = Rate
        fields = ("source", "currency")


class SourceFilter(FilterSet):
    class Meta:
        model = Source
        fields = ("url", "name")


class ContactUsFilter(FilterSet):
    class Meta:
        model = ContactUs
        fields = ("email_from", "subject")


class LoggingFilter(FilterSet):
    class Meta:
        model = RequestResponseLog
        fields = ("method", "status_code", "time")