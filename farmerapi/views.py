from rest_framework import generics
from farmer.models import Yards,Items
from .serializers import YardSerializer,ItemSerializer
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS,IsAuthenticatedOrReadOnly


class YardUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class YardList(generics.ListCreateAPIView,YardUserWritePermission):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Yards.yardobjects.all()
    serializer_class = YardSerializer

class YardDetail(generics.RetrieveUpdateDestroyAPIView, YardUserWritePermission):
    permission_classes = [YardUserWritePermission]
    queryset = Yards.yardobjects.all()
    serializer_class = YardSerializer

class ItemUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.itemproducer == request.user

class ItemList(generics.ListCreateAPIView,ItemUserWritePermission):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Items.itemobjects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView, ItemUserWritePermission):
    permission_classes = [ItemUserWritePermission]
    queryset = Items.itemobjects.all()
    serializer_class = ItemSerializer


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
