# from django.core.mail import send_mail
# from rest_framework import status
from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from support.models import Contact
from support.serializers import ContactSerializer


class ContactView(CreateAPIView):

    queryset = Contact.objects.all()
    print('Contact Queryset: ', queryset)
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)
    name = 'support-contact-list'
    # filterset_class = TransactionLogFilter
    # ordering_fields = ('name',)
    # lookup_field = 'pk'
    # ordering = ('reference',)
    ordering = ('-created_at',)
    # search_fields = ('reference',)
    # renderer_classes = (ServiceJSONRenderer,)

    # def post(self, request, *args, **kwargs):
    #     serializer = ContactSerializer(request.data)
    #     if serializer.is_valid():
    #         data = serializer.validated_data
    #         email = data.get('email')
    #         name = data.get('name')
    #         send_mail(
    #             'Sent email from {}'.format(name),
    #             'Here is the message. {}'.format(serializer.validated_data.get('message')),
    #             email,
    #             ['to@example.com'],
    #             fail_silently=False, )
    #
    #         return Response({"success": "Sent"})
    #
    #     return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)
