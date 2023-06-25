from django.urls import path
from currency import views

urlpatterns = [
    path('', views.home_view),
    path('contactus/list/', views.contactus_list),
]