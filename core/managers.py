from django.db import models
from datetime import datetime, timedelta
#
# # First, define the Manager subclass.
# class DahlBookManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(author='Roald Dahl')


class SoftDeleteManager(models.Manager):
    ''' Use this manager to get objects that have a deleted field '''

    def get_queryset(self):
        return super(SoftDeleteManager, self).get_queryset().filter(deleted_at__isnull=True)
        # return super(SoftDeleteManager, self).get_query_set().filter(deleted_at__isnull=False)

    def all_with_trashed(self):
        return super(SoftDeleteManager, self).get_queryset()

    def trashed_set(self):
        return super(SoftDeleteManager, self).get_queryset().filter(deleted_at__isnull=False)

    def trashed_within_days_set(self, days):
        return super(SoftDeleteManager, self).get_queryset()\
            .filter(deleted_at__gte=datetime.now() - timedelta(days=days))
        # .filter(deleted_at__isnull=False)
