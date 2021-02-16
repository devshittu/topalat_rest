from django.contrib import admin
from services.models import TransactionLog


class TransactionLogAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'reference',
        'description',
        'service_category_raw',
        'service_provider_raw',
        'reference',
        'payment_status',
        'service_render_status',
        'service_request_payload_data'
    )


admin.site.register(TransactionLog, TransactionLogAdmin)
