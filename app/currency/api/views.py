from rest_framework.generics import ListAPIView
from currency.models import Rate, ContactUs, Source, RequestResponseLog
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def demo_view(request):
    return Response({"message": "Hello, World"})


class RatesListAPIView(ListAPIView):
    ...