from django.urls import path
from currency import views

urlpatterns = [
    path('', views.home_view),
    path('contacts/json/', views.contacts_json, name='contacts_json'),
    path('rates/json/', views.rates_json, name='rates_json'),
    path('rates/table/', views.rates_table, name='rates_table'),
]
