from django.contrib.postgres.fields import HStoreField
from django.core.validators import MaxValueValidator
from django.db import models
from core.models import SoftDeleteModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _

from core.constants import PAYMENT_STATUSES, DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED


class TransactionLog(TimeStampedModel, SoftDeleteModel):
    email = models.EmailField(_('customer email address'))
    reference = models.CharField(unique=True, db_index=True, max_length=32)
    description = models.CharField(max_length=200, blank=True, null=True)
    service_category_raw = models.CharField(max_length=80, blank=True, null=True)
    service_provider_raw = models.CharField(max_length=80, blank=True, null=True)

    payment_status = models.IntegerField(choices=PAYMENT_STATUSES,
                                         default=DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED)
    service_render_status = models.IntegerField(choices=PAYMENT_STATUSES,
                                                default=DBCV_PAYMENT_SERVICE_STATUS_UNPROCESSED,
                                                )
    service_request_payload_data = HStoreField()

    def __unicode__(self):
        return u'{0}'.format(self.reference)

    class Meta:
        verbose_name = _('transaction_log')
        verbose_name_plural = _('transaction_logs')
