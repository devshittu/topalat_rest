from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from core.mixins import SoftCreateMixin, SoftUpdateMixin, SoftDeleteMixin


class MyListCreateAPIView(ListCreateAPIView, SoftCreateMixin):

    # def post(self, request, *args, **kwargs):
    #     print('MyListCreateAPIView://request', request.user )
    #     if request.user:
    #         self.perform_create(user=self.request.user)
    #     else:
    #         return self.create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class MyAuthedListCreateAPIView(ListCreateAPIView, SoftCreateMixin):
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class MyRetrieveUpdateAPIView(RetrieveUpdateAPIView, SoftUpdateMixin):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # request.data['published_by'] = request.user
        print('MyRetrieveUpdateAPIView:// ', request.data)
        return self.partial_update(request, *args, **kwargs)


class MyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView, SoftUpdateMixin, SoftDeleteMixin):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MyRetrieveAPIView(RetrieveAPIView):
    pass


class MyUpdateAPIView(UpdateAPIView):
    pass

class MyListAPIView(ListAPIView):
    pass
