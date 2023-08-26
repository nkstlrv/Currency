from rest_framework import viewsets
from currency.models import Rate, ContactUs, Source, RequestResponseLog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RateSerializer, SourceSerializer, ContactUsSerializer, LoggingSerializer
from .paginators import MainPagination
from .filters import RateFilter, SourceFilter, ContactUs
from rest_framework import filters as rest_framework_filters
from django_filters import rest_framework as filters


@api_view(['GET'])
def demo_view(request):
    return Response({"message": "Hello, World"})


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-id')
    serializer_class = RateSerializer
    pagination_class = MainPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = ('buy', 'sell', 'created')


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all().order_by('-id')
    serializer_class = SourceSerializer
    pagination_class = MainPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = SourceFilter
    ordering_fields = ('name', 'url')