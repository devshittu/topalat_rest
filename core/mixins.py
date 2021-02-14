from django.db import IntegrityError
from pprint import pprint
from rest_framework import status, generics
from rest_framework.response import Response


class SoftDeleteMixin(generics.DestroyAPIView):
    """
    Destroy a model instance.
    """

    def soft_delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.soft_delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.soft_delete()


class SoftUpdateMixin(generics.UpdateAPIView):

    def update(self, request, *args, **kwargs):
        try:
            return super(SoftUpdateMixin, self).update(request, *args, **kwargs)
        except IntegrityError as e:
            message = 'Integrity error. The name already exists. '
            # message = 'Integrity error. The name already exists. ' + str(e)
            content = {'detail': message}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        try:
            return super(SoftUpdateMixin, self).partial_update(request, *args, **kwargs)
        except IntegrityError as e:
            message = 'Integrity error. The name already exists. '
            # message = 'Integrity error. The name already exists. ' + str(e)
            # You don't need to use the str(e). It is just for you to know what is going on.
            content = {'detail': message}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SoftCreateMixin(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        # return super(SoftCreateMixin, self).create(request, *args, **kwargs)
        try:
            return super(SoftCreateMixin, self).create(request, *args, **kwargs)
        except IntegrityError as e:
            # message = 'Integrity error. The name already exists. '
            message = 'Integrity error. The name already exists. ' + str(e)
            # You don't need to use the str(e). It is just for you to know what is going on.
            content = {'detail': message}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To set the owner to the user received in the request
        fields = serializer.get_fields()
        # print('serializer:perform_create:/fields:/', fields)
        check_user_in_fields = 'user' in fields

        # print('check_user_in_fields = ', check_user_in_fields)

        if self.request.user.id is not None and check_user_in_fields:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
