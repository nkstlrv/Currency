from django.urls import path
from currency.views import home_view

urlpatterns = [
    path('', home_view),
]