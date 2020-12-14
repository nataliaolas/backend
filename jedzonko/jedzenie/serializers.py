from rest_framework import serializers
from jedzenie.models import Pozycja,Restauracja,Adres,Menu,TypRestauracji,Klient,Zamowienie,Wlasciciel, OpiniaORestauracji

class PozycjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pozycja
        fields='__all__'

class RestauracjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restauracja 
        fields ='__all__'

class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    pozycje = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = ['restauracja', 'pozycje']



class TypRestauracjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypRestauracji
        fields = '__all__'

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'

class ZamowienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'

class WlascicielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wlasciciel
        fields = '__all__'

class OpiniaORestauracjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpiniaORestauracji
        fields = '__all__'