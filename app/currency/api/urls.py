from currency.api import views
from django.urls import path

app_name = "currency_api"


urlpatterns = [
    path("rate/list/", views.RatesListAPIView.as_view(), name="api-rate-list")
]