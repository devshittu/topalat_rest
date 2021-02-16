from django.contrib.auth import get_user_model
from django.core import validators
from rest_framework import serializers

from core.constants import PAYMENT_STATUSES
from .models import TransactionLog

User = get_user_model()


class TransactionLogSerializer(serializers.HyperlinkedModelSerializer):
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    email = serializers.CharField(required=True)
    reference = serializers.CharField(required=True)
    service_category_raw = serializers.CharField(required=True)
    service_provider_raw = serializers.CharField(required=False)
    payment_status = serializers.ChoiceField(choices=PAYMENT_STATUSES)
    service_render_status = serializers.ChoiceField(choices=PAYMENT_STATUSES)
    service_request_payload_data = serializers.HStoreField(required=True)

    class Meta:
        model = TransactionLog
        fields = (
            'id',
            'updated_at',
            'created_at',
            'email',
            'reference',
            'service_category_raw',
            'service_provider_raw',
            'payment_status',
            'service_render_status',
            'service_request_payload_data')
