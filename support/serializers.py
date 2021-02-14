from rest_framework import serializers
from django.core.mail import send_mail
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
        send_mail(
            'Instance {} has been created'.format(instance.pk),
            'Here is the message. DATA: {}'.format(validate_data),
            'from@example.com',
            ['support@example.com'],
            fail_silently=False,
        )
        return instance
