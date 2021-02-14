from django.conf.urls import url
from django.urls import path

from . import views
from rest_framework.authtoken import views as rest_auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^auth/register/$',
        views.RegistrationAPIView.as_view(),
        name=views.RegistrationAPIView.name),
    url(r'^auth/login/$',
        views.LoginAPIView.as_view(),
        name=views.LoginAPIView.name),
    url(r'^auth/me',
        views.UserRetrieveUpdateAPIView.as_view(),
        name=views.UserRetrieveUpdateAPIView.name),
    url(r'^auth/user/(?P<pk>[0-9]+)/$',
        views.UserRetrieveAPIView.as_view(),
        name=views.UserRetrieveAPIView.name),
    path('auth/users/',
         views.UserList.as_view(),
         name=views.UserList.name),

    url(r'^go/(?P<username>[\w-]+)/$',
        views.UserByUsernameRetrieveAPIView.as_view(),
        name=views.UserByUsernameRetrieveAPIView.name),

    path('check/<slug:username>/',
         views.CheckUsernameExistsRetrieveAPIView.as_view(),
         name=views.CheckUsernameExistsRetrieveAPIView.name),

    path('auth/get-token/', rest_auth_views.obtain_auth_token, name='api-token-auth'),
    path('auth/signin/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    # path('logout', Views.Logout.as_view()),


]
