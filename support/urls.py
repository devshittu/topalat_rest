from django.urls import path

from . import views

urlpatterns = [
    # path('services/providers/<str:code_name>/',
    #      views.ServiceProviderDetail.as_view(),
    #      name=views.ServiceProviderDetail.name),
    path('contact/',
         views.ContactView.as_view(),
         name=views.ContactView.name),


]
