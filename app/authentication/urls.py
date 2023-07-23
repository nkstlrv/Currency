from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProgileView.as_view(), name='profile'),
    ]