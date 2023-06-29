from django.urls import path
from currency import views

urlpatterns = [
    path('', views.home_view),
    path('contacts/json/', views.contacts_json),
    path('contacts/table/', views.contacts_table),
]
