from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.


def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
