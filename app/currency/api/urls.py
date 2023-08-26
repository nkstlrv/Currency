from currency.api import views
from django.urls import path

app_name = "currency_api"


urlpatterns = [
    path("demo/", views.demo_view, name="api-demo"),
    path("rate/list/", views.RatesListAPIView.as_view(), name="api-rate-list"),
]