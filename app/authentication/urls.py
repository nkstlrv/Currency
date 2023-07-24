from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProgileView.as_view(), name='profile'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password-change/<int:pk>/', views.PasswordChangeView.as_view(), name='password-change'),
    ]