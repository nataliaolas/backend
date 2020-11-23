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
