from rest_framework import mixins
from rest_framework import viewsets
from .models import (Pozycja,
                     Restauracja,
                     Adres,
                     Menu,
                     TypRestauracji,
                     Klient,
                     Zamowienie,
                     Wlasciciel,
                     OpiniaORestauracji)
from .serializers import PozycjaSerializer, \
    RestauracjaSerializer, AdresSerializer, \
    MenuSerializer, TypRestauracjiSerializer, KlientSerializer, \
    ZamowienieSerializer, WlascicielSerializer, OpiniaORestauracjiSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class RestauracjaView(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Restauracja.objects.all()
    serializer_class = RestauracjaSerializer


class TypRestauracjiView(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = TypRestauracji.objects.all()
    serializer_class = TypRestauracjiSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nazwa']
    ordering = ['nazwa']

class WlascicielView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Wlasciciel.objects.all()
    serializer_class = WlascicielSerializer


class AdresView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['miasto']

class KlientlView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class PozycjaView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Pozycja.objects.all()
    serializer_class = PozycjaSerializer


class MenuView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OpiniaORestauracjiView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = OpiniaORestauracjiSerializer

class ZamowienieView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = ZamowienieSerializer    
