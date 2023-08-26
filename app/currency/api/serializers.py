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


class SourceSerializer(Serializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'url',
            'dev_name',
        )


class ContactUsSerializer(Serializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
        )


class LoggingSerializer(Serializer):
    class Meta:
        model = RequestResponseLog
        fields = (
            'id',
            'path',
            'method',
            'status_code',
            'created',
            'time',
        )
