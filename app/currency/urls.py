from django.urls import path
from currency import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contacts/json/', views.contacts_json, name='contacts_json'),
    path('contacts/table/', views.contacts_table, name='contacts_table'),
    path('rates/json/', views.rates_json, name='rates_json'),
    path('rates/table/', views.rates_table, name='rates_table'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/update/<int:pk>/', views.contact_update, name='contact_update'),
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    path('rates/create/', views.rate_create, name='rate_create'),
    path('rates/update/<int:pk>/', views.rate_update, name='rate_update'),
    path('rates/delete/<int:pk>/', views.rate_delete, name='rate_delete'),
    path('sources/table/', views.sources_table, name='sources_table'),
    path('sources/create/', views.source_create, name='source_create'),
]
