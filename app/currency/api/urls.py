from currency.api import views
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "currency_api"

router = DefaultRouter(trailing_slash=False)
router.register('rate/', views.RateViewSet, basename='rate')
router.register('source/', views.SourceViewSet, basename='source')
router.register('contact-us/', views.ContactUsViewSet, basename='contact-us')
router.register('logging/', views.LoggingViewSet, basename='logging')


urlpatterns = [
    path("rate/detail-delete/<int:pk>/", views.RateDetailDestroyApiView.as_view(), name='rate-detail-delete'),
]

urlpatterns += router.urls