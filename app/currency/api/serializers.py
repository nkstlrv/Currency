from rest_framework.serializers import ModelSerializer
from currency.models import Rate, Source, ContactUs, RequestResponseLog


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'source',
        )


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'url',
            'dev_name',
        )


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
        )


class LoggingSerializer(ModelSerializer):
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
