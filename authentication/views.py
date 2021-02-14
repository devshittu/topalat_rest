from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from authentication.renderers import UserJSONRenderer
from authentication.serializers import RegistrationSerializer, LoginSerializer, UserSerializer, \
    StaffRegistrationSerializer
from core.permissions import IsSuperUserOrReadOnly
from core.views import MyRetrieveUpdateAPIView, MyListCreateAPIView

User = get_user_model()


# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     name = 'category-list'
#     filterset_class = CategoryFilter
#     # ordering_fields = ('name',)
#     ordering = ('name',)
#     search_fields = ('name',)


class RegistrationAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    name = 'register'
    renderer_classes = (UserJSONRenderer,)
    # serializer_class = RegistrationSerializer
    serializer_class = StaffRegistrationSerializer

    # def post(self, request):
    #     user = request.data.get('user', {})
    #     print('Prepping the data b4 submission', )
    #     print(request.data, user)
    #     # The create serializer, validate serializer, save serializer pattern
    #     # below is common and you will see it a lot throughout this course and
    #     # your own work later on. Get familiar with it.
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserList(MyListCreateAPIView):
    queryset = User.objects.all()
    print('Queryset: ', queryset)
    serializer_class = UserSerializer
    # permission_classes = (AllowAny,)
    name = 'user-list'
    # filterset_class = TransactionLogFilter
    # ordering_fields = ('name',)
    # lookup_field = 'pk'
    # ordering = ('reference',)
    # ordering = ('-created_at', )
    search_fields = ('email',)
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (
        IsSuperUserOrReadOnly,
    )


class LoginAPIView(generics.GenericAPIView):
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    name = 'login'

    def post(self, request):
        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# this is for in authenticated user only
class UserRetrieveUpdateAPIView(MyRetrieveUpdateAPIView):
    # TODO activate permission class
    permission_classes = (IsAuthenticated, ) #IsOwnerOrReadOnly
    renderer_classes = (UserJSONRenderer,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    lookup_field = 'pk'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
        # return get_object_or_404(User, pk=request.session['user_id'])


# This is for general users
class UserRetrieveAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser,)
    renderer_classes = (UserJSONRenderer,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users-detail'
    lookup_field = 'pk'


# This is for general users by username
class UserByUsernameRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users-page'
    lookup_field = 'username'


# This is for general users by username
class CheckUsernameExistsRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    name = 'users-exist-page'
    lookup_field = 'username'

    def get(self, request, *args, **kwargs):
        # use this if username is in url kwargs
        username = self.kwargs.get('username')

        # use this if username is being sent as a query parameter
        # username = self.request.query_params.get('username')

        try:
            user = User.objects.get(username=username)  # retrieve the user using username
        except User.DoesNotExist:
            return Response(data={'exist': False})  # return false as user does not exist
        else:
            return Response(data={'exist': True})  # Otherwise, return True
