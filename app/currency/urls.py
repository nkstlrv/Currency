from django.urls import path
from currency import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contacts/json/', views.contacts_json, name='contacts_json'),
    path('contacts/table/', views.contacts_table, name='contacts_table'),
    path('rates/json/', views.rates_json, name='rates_json'),
    path('rates/table/', views.rates_table, name='rates_table'),
]
