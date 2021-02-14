from django.urls import path

from . import views

urlpatterns = [
    path('services/categories/',
         views.ServiceCategoryList.as_view(),
         name=views.ServiceCategoryList.name),
    path('services/categories/<str:code_name>/',
         views.ServiceCategoryDetail.as_view(),
         name=views.ServiceCategoryDetail.name),
    # path('services/categories/<int:pk>/',
    #      views.ServiceCategoryDetail.as_view(),
    #      name=views.ServiceCategoryDetail.name),
    path('services/providers/',
         views.ServiceProviderList.as_view(),
         name=views.ServiceProviderList.name),
    path('services/providers/<str:code_name>/',
         views.ServiceProviderDetail.as_view(),
         name=views.ServiceProviderDetail.name),
    path('services/transactionlogs/',
         views.TransactionLogList.as_view(),
         name=views.TransactionLogList.name),


    path('services/transactionlogs/<str:reference>/',
         views.TransactionLogDetail.as_view(),
         name=views.TransactionLogDetail.name),

    # path('books/<publisher>/', PublisherBookList.as_view()),
    path('services/transactionlogs/category/<category>/',
         views.TransactionLogByCategoryList.as_view(),
         name=views.TransactionLogByCategoryList.name),

]
