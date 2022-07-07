from .views import YardList,YardDetail,ItemDetail,ItemList
from django.urls import path

urlpatterns = [
    path('Yards/<int:pk>/',YardDetail.as_view(),name = 'detailcreate'),
    path('Yards',YardList.as_view(),name='listcreate'),
    path('Items/<int:pk>/',ItemDetail.as_view(),name = 'detailcreate'),
    path('Items/',ItemList.as_view(),name='listcreate'),
]
