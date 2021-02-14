from django.conf.urls import url
from django.urls import path

from authentication.views import MA_ObtainEmailCallbackToken, MA_ObtainMobileCallbackToken
from . import views
from rest_framework.authtoken import views as rest_auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('webhook/', MA_ObtainEmailCallbackToken.as_view(), name='auth_email'),
    # path('auth/mobile/', MA_ObtainMobileCallbackToken.as_view(), name='auth_mobile'),

    # url(r'^webhook', views.webhook, name='webhook'),
]
