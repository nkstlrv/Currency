from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from currency.models import Rate, ContactUs, Source, RequestResponseLog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RateSerializer, SourceSerializer, ContactUsSerializer, LoggingSerializer
from .paginators import RatePagination
from .filters import RateFilter, SourceFilter, ContactUs
from rest_framework import filters as rest_framework_filters
from django_filters import rest_framework as filters


@api_view(['GET'])
def demo_view(request):
    return Response({"message": "Hello, World"})


class RateListAPIView(ListAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter


class RateDetailAPIView(RetrieveUpdateAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer


class SourceCreateAPIView(CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def create(self, request, *args, **kwargs):
        ...


class RateCreateAPIView(CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def create(self, request, *args, **kwargs):
        ...
