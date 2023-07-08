from django.urls import path
from currency import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    
    path('contacts/json/', views.contacts_json, name='contacts_json'),
    path('contacts/table/', views.ContactsListView.as_view(), name='contacts_table'),
    
    path('rates/json/', views.rates_json, name='rates_json'),
    path('rates/table/', views.RatesListView.as_view(), name='rates_table'),
    
    path('contacts/create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contacts/update/<int:pk>/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contacts/delete/<int:pk>/', views.ContactDeleteView.as_view(), name='contact_delete'),
    
    path('rates/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rates/update/<int:pk>/', views.rate_update, name='rate_update'),
    path('rates/delete/<int:pk>/', views.rate_delete, name='rate_delete'),
    
    path('sources/table/', views.sources_table, name='sources_table'),
    path('sources/create/', views.source_create, name='source_create'),
    path('sources/update/<int:pk>/', views.source_update, name='source_update'),
    path('sources/delete/<int:pk>/', views.source_delete, name='source_delete'),
]
