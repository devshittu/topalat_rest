from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from core.managers import SoftDeleteManager


class UserTimeStampedModel(models.Model):
    # A timestamp representing when this object was created.
    joined_at = models.DateTimeField(default=timezone.now, editable=False)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='updated at', editable=False)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        # print('self:// ', type(self), self.pk)
        if not self.pk:
            self.joined_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        return super(UserTimeStampedModel, self).save(*args, **kwargs)


class TimeStampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='updated at', editable=False)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.pk:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        return super(TimeStampedModel, self).save(*args, **kwargs)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='deleted at')

    # MANAGERS
    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    # Here's where to take a look
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
