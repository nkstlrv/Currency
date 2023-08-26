from rest_framework.serializers import ModelSerializer
from currency.models import Rate, Source, ContactUs, RequestResponseLog
from currency.tasks import send_email_contact_us


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
            'name',
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

    def create(self, validated_data):
        instance = super().create(validated_data)

        # Sending email to Customer support
        send_email_contact_us.delay(validated_data)

        return instance


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
