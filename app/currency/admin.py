from django.contrib import admin
from currency.models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'currency',
        'source',
        'created',
    )
    list_filter = (
        'currency',
        ('created')
    )
    search_fields = (
        'buy',
        'sell',
        'source',
    )

    def has_delete_permission(self, request, obj=None):
        return False

