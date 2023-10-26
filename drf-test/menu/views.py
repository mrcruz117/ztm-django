from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ItemSerializer, ItemCreateSerializer,  UserSerializer, UserCreateSerializer, Source_locationSerializer
from .models import Item, User, Source_location

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ItemCreateSerializer
        # if self.action == 'list':
        return ItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return UserCreateSerializer
        # if self.action == 'list':
        return UserSerializer


class Source_locationViewSet(viewsets.ModelViewSet):
    queryset = Source_location.objects.all()
    serializer_class = Source_locationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['address', 'id']
    search_fields = ['address']
    ordering_fields = ['address']

    def get_serializer_context(self):
        return {'request': self.request}


def item_list_NOT_SERIALIZED(request):
    items = Item.objects.all()
    item_list = []
    for item in items:
        item_list.append({
            'name': item.name,
            'price': item.price,
            'description': item.description
        })
    return JsonResponse({"menu_items": item_list})


@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serialized_items = ItemSerializer(items, many=True)
    return Response(serialized_items.data)


@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    serialized_item = ItemSerializer(item)
    return Response(serialized_item.data)
