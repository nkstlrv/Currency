import django_filters
from .models import Rate


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = ("source", "currency")
