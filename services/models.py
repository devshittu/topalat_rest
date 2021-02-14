from django.contrib.postgres.fields import HStoreField
from django.core.validators import MaxValueValidator
from django.db import models
from core.models import SoftDeleteModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _

from core.constants import PAYMENT_STATUSES, DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED, DBCV_SERVICE_TYPE_AIRTIME, \
    SERVICE_TYPES


# Create your models here.

class ServiceCategory(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=80, blank=True, null=True)
    code_name = models.SlugField(max_length=50, unique=True, db_index=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'service_category'
        verbose_name_plural = 'service_categories'

    def __str__(self):
        return self.name


class ServiceProvider(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=80, blank=True, null=True)
    code_name = models.SlugField(max_length=50, unique=True, db_index=True)
    is_available = models.BooleanField(default=True)

    # service_category = models.ForeignKey(
    #     ServiceCategory,
    #     on_delete=models.DO_NOTHING,
    #     related_name='service_providers',
    # )

    # mtn, dstv, kedco

    class Meta:
        ordering = ('name',)
        verbose_name = 'service_provider'
        verbose_name_plural = 'services_providers'

    def __str__(self):
        return self.name


class TransactionLog(TimeStampedModel, SoftDeleteModel):
    email = models.EmailField(_('customer email address'))
    reference = models.CharField(unique=True, db_index=True, max_length=32)
    description = models.CharField(max_length=80, blank=True, null=True)
    service_category_raw = models.CharField(max_length=80, blank=True, null=True)
    service_provider_raw = models.CharField(max_length=80, blank=True, null=True)

    service_type = models.CharField(max_length=5, choices=SERVICE_TYPES,
                                    default=DBCV_SERVICE_TYPE_AIRTIME)
    payment_status = models.IntegerField(choices=PAYMENT_STATUSES,
                                         default=DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED)
    service_render_status = models.IntegerField(choices=PAYMENT_STATUSES,
                                                default=DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED,
                                                )
    service_request_payload_data = HStoreField()
    # service_provider = models.ForeignKey(
    #     ServiceProvider,
    #     on_delete=models.DO_NOTHING,
    #     related_name='transaction_logs',
    # )

    def __unicode__(self):
        return u'{0}'.format(self.reference)

    class Meta:
        verbose_name = _('transaction_log')
        verbose_name_plural = _('transaction_logs')
