from rest_framework import viewsets
from rest_framework import generics
from currency.models import Rate, ContactUs, Source, RequestResponseLog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RateSerializer, SourceSerializer, ContactUsSerializer, LoggingSerializer
from .paginators import MainPagination
from .filters import RateFilter, SourceFilter, ContactUsFilter, LoggingFilter
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


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-id')
    serializer_class = ContactUsSerializer
    pagination_class = MainPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = ContactUsFilter
    ordering_fields = ('subject', 'email_from')


class LoggingViewSet(viewsets.ModelViewSet):
    queryset = RequestResponseLog.objects.all().order_by('-id')
    serializer_class = LoggingSerializer
    pagination_class = MainPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = LoggingFilter
    ordering_fields = ('method', 'path', "time", "created")


class RateDetailDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()


class SourceDetailDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()


class ContactUsDetailDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()


class LoggsUsDetailDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = LoggingSerializer
    queryset = RequestResponseLog.objects.all()
