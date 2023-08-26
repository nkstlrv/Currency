from currency.api import views
from django.urls import path

app_name = "currency_api"


urlpatterns = [
    path("demo/", views.demo_view, name="api-demo"),
    path("rate/list/", views.RateListAPIView.as_view(), name="api-rate-list"),
    path("rate/<int:pk>/", views.RateDetailAPIView.as_view(), name="api-rate-detail"),
]