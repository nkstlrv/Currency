from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProgileView.as_view(), name='profile'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    ]