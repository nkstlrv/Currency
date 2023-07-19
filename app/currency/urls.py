from django.urls import path
from currency import views

urlpatterns = [
    path(
        "sources/delete/<int:pk>/",
        views.SourceDeleteView.as_view(),
        name="source_delete",
    ),
    path(
        "sources/update/<int:pk>/",
        views.SourceUpdateView.as_view(),
        name="source_update",
    ),
    path("sources/create/", views.SourceCreateView.as_view(), name="source_create"),
    path("sources/table/", views.SourcesListView.as_view(), name="sources_table"),
    path(
        "contacts/delete/<int:pk>/",
        views.ContactDeleteView.as_view(),
        name="contact_delete",
    ),
    path(
        "contacts/update/<int:pk>/",
        views.ContactUpdateView.as_view(),
        name="contact_update",
    ),
    path("contacts/create/", views.ContactCreateView.as_view(), name="contact_create"),
    path("contacts/table/", views.ContactsListView.as_view(), name="contacts_table"),
    path("rates/delete/<int:pk>/", views.RateDeleteView.as_view(), name="rate_delete"),
    path("rates/update/<int:pk>/", views.RateUpdateView.as_view(), name="rate_update"),
    path("rates/create/", views.RateCreateView.as_view(), name="rate_create"),
    path("rates/table/", views.RatesListView.as_view(), name="rates_table"),
    path("contacts/json/", views.contacts_json, name="contacts_json"),
    path("rates/json/", views.rates_json, name="rates_json"),
    path("", views.HomeTemplateView.as_view(), name="home"),
]
