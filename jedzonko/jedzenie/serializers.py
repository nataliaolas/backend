from django.contrib.auth.models import User
from rest_framework import serializers
from jedzenie.models import Pozycja,Restauracja,Adres,Menu,TypRestauracji,Klient,Zamowienie,Wlasciciel, OpiniaORestauracji,Platnosc

class PozycjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pozycja
        fields='__all__'

class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'

class TypRestauracjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypRestauracji
        fields = '__all__'


class RestauracjaSerializer(serializers.ModelSerializer):
    srednia_opinia_o_restauracji = serializers.SerializerMethodField()
    adresy = AdresSerializer(many=False)
    class Meta:
        model = Restauracja 
        fields ='__all__'

    def get_srednia_opinia_o_restauracji(self, obj):
        return obj.get_srednia_z_opinii()

    def create(self, validated_data):
        ordered_dict = validated_data['adresy']
        new_adres = Adres()
        new_adres.miasto = ordered_dict['miasto']
        new_adres.ulica = ordered_dict['ulica']
        new_adres.nr_budynku = ordered_dict['nr_budynku']
        try:
            new_adres.nr_mieszkania = ordered_dict['nr_mieszkania']
        except:
            pass
        validated_data['adresy'] = new_adres
        new_adres.save()
        print("ordered",ordered_dict)
        restauracja = Restauracja.objects.create(**validated_data)
        return restauracja


class MenuSerializer(serializers.ModelSerializer):
    pozycje = PozycjaSerializer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = ['restauracja', 'pozycje']


class KlientSerializer(serializers.ModelSerializer):
    adres = AdresSerializer(many=False)
    class Meta:
        model = Klient
        fields = '__all__'

    def create(self, validated_data):
        ordered_dict = validated_data['adres']
        new_adres = Adres()
        new_adres.miasto = ordered_dict['miasto']
        new_adres.ulica = ordered_dict['ulica']
        new_adres.nr_budynku = ordered_dict['nr_budynku']
        new_adres.nr_mieszkania = ordered_dict['nr_mieszkania']
        validated_data['adres'] = new_adres
        new_adres.save()
        print("validated_data: ", validated_data)
        print("*****\n\n\n*************\n\n\n\n")
        klient = Klient.objects.create(**validated_data)
        return klient

class ZamowienieSerializer(serializers.ModelSerializer):
    # pozycje = PozycjaSerializer(many=True,read_only=True)
    class Meta:
        model = Zamowienie
        fields = '__all__'

    # def create(self, validated_data):
    #     ordered_dict = validated_data['pozycje']
    #     new_adres = Pozycja()
    #     new_adres.nazwadania = ordered_dict['nazwadania']
    #     new_adres.sklad = ordered_dict['sklad']
    #     validated_data['pozycje'] = new_adres
    #     new_adres.save()
    #     print("ordered",ordered_dict)
    #     zamowienie = Zamowienie.objects.create(**validated_data)
    #     return zamowienie
        
class WlascicielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wlasciciel
        fields = '__all__'

class OpiniaORestauracjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpiniaORestauracji
        fields = '__all__'

class PlatnoscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosc
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User()
        user.username = validated_data['username']
        user.email = validated_data['email']
        user.password = validated_data['password']
        user.save()
        return user