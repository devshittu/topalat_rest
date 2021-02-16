from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'phone',
            'subject',
            'message',
        )

    def create(self, validate_data):
        instance = super(ContactSerializer, self).create(validate_data)
        # settings.EMAIL_HOST_USER
        subject = 'Instance {} has been created'.format(instance.subject),
        message = 'Here is the message. DATA: {}'.format(validate_data),
        email_from = instance.email
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False,)

        # send_mail(
        #     'Instance {} has been created'.format(instance.pk),
        #     'Here is the message. DATA: {}'.format(validate_data),
        #     'from@example.com',
        #     ['support@example.com'],
        #     fail_silently=False,
        # )
        return instance
