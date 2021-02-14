from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'support_contact'
        verbose_name_plural = 'service_contacts'

    def __str__(self):
        return self.name
