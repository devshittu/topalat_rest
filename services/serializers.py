from django.contrib.auth import get_user_model
from django.core import validators
from rest_framework import serializers

from core.constants import PAYMENT_STATUSES
from .models import TransactionLog, ServiceCategory, ServiceProvider

User = get_user_model()


class ServiceCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    code_name = serializers.SlugField()
    is_available = serializers.BooleanField()
    # transaction_log = serializers.HyperlinkedRelatedField(many=True, read_only=True)
    # stories = StorySerializer()

    class Meta:
        model = ServiceCategory
        fields = (
            'id',
            'name',
            'description',
            'code_name',
            'is_available',
        )


class ServiceProviderSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    description = serializers.CharField()
    service_category = serializers.CharField()
    code_name = serializers.SlugField()
    is_available = serializers.BooleanField()

    class Meta:
        model = ServiceCategory
        fields = (
            'id',
            'name',
            'description',
            'service_category',
            'code_name',
            'is_available',
        )


class TransactionLogSerializer(serializers.HyperlinkedModelSerializer):
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    email = serializers.CharField(required=True)
    reference = serializers.CharField(required=True)
    service_category_raw = serializers.CharField(required=True)
    # service_provider = serializers.CharField(required=True)
    # service_provider = ServiceProviderSerializer()
    # service_provider = serializers.SlugRelatedField(queryset=ServiceProvider.objects.all(), slug_field='code_name')
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
            'service_type',
            'service_category_raw',
            # 'service_provider',
            'payment_status',
            'service_render_status',
            'service_request_payload_data')
