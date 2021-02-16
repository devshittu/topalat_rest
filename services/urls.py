from django.urls import path

from . import views

urlpatterns = [
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
