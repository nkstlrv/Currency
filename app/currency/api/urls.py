from currency.api import views
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "currency_api"

router = DefaultRouter(trailing_slash=False)
router.register("rate/", views.RateViewSet, basename="rate")
router.register("source/", views.SourceViewSet, basename="source")
router.register("contact-us/", views.ContactUsViewSet, basename="contact-us")
router.register("logging/", views.LoggingViewSet, basename="logging")


urlpatterns = [
    path(
        "rate/detail-delete/<int:pk>/",
        views.RateDetailDestroyApiView.as_view(),
        name="rate-detail-delete",
    ),
    path(
        "source/detail-delete/<int:pk>/",
        views.SourceDetailDestroyApiView.as_view(),
        name="source-detail-delete",
    ),
    path(
        "contactus/detail-delete/<int:pk>/",
        views.ContactUsDetailDestroyApiView.as_view(),
        name="contactus-detail-delete",
    ),
    path(
        "loggs/detail-delete/<int:pk>/",
        views.LoggsUsDetailDestroyApiView.as_view(),
        name="loggs-detail-delete",
    ),
]

urlpatterns += router.urls
