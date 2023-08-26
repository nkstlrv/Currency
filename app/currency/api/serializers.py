from rest_framework.serializers import Serializer
from currency.models import Rate, Source, ContactUs, RequestResponseLog


class RateSerializer(Serializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'source',
        )
