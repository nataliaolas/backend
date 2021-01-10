from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
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
        fields = ['id','restauracja', 'pozycje']
    



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
    pozycje = PozycjaSerializer(many=True,read_only=True)
    class Meta:
        model = Zamowienie
        fields = '__all__'

    def create(self, validated_data):
        ordered_dict = validated_data['pozycje']
        new_adres = Pozycja()
        new_adres.nazwadania = ordered_dict['nazwadania']
        new_adres.sklad = ordered_dict['sklad']
        validated_data['pozycje'] = new_adres
        new_adres.save()
        print("ordered",ordered_dict)
        zamowienie = Zamowienie.objects.create(**validated_data)
        return zamowienie
        
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
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email','username', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Złe dane logowania")