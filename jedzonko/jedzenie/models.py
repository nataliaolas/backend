from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Pozycja(models.Model):
    cena = models.FloatField()
    nazwadania = models.CharField(max_length=50)
    sklad = models.TextField()
    menu = models.ForeignKey('Menu',related_name='pozycje', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nazwa +" "+ str(self.cena) +" " + self.sklad

def upload_to(instance,filename):
    return 'posts/{filename}'.format(filename=filename)

class Restauracja(models.Model):
    zdjecie = models.ImageField(_("Image"),upload_to="restauracje",default=False)
    nazwa = models.CharField(max_length=30,default=False)
    opis = models.TextField(null=True)
    adresy = models.ForeignKey('Adres', on_delete=models.SET_NULL, null=True)
    wlasciciel = models.ForeignKey('Wlasciciel', on_delete=models.CASCADE, null=True)
    typ_restauracji = models.ForeignKey("TypRestauracji", on_delete=models.SET_NULL, null=True)

    def get_srednia_z_opinii(self):
        opinie = self.opinie.all()
        srednia_z_opinii = 0
        if opinie:
            suma_opinii = 0
            for opinia in opinie:
                suma_opinii += opinia.zadowolenie_klienta
            srednia_z_opinii = suma_opinii/opinie.count()
        return srednia_z_opinii


class Adres(models.Model):
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)
    nr_budynku = models.IntegerField()
    nr_mieszkania= models.IntegerField(blank=True,null=True)


class Menu(models.Model):
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE, null=True)


class TypRestauracji(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Klient(models.Model):
    adres = models.ForeignKey(Adres, on_delete=models.CASCADE)
    mail = models.CharField(max_length=30)
    nr_telefonu = models.IntegerField()


class Zamowienie(models.Model):
    cena_zamowienia = models.FloatField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    przyblizony_czas_dostawy = models.IntegerField()
    pozycje = models.ManyToManyField(Pozycja)


class Wlasciciel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class OpiniaORestauracji(models.Model):
    opis = models.TextField()
    zadowolenie_klienta = models.IntegerField()
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE, null=True, related_name="opinie")

class Platnosc(models.Model):
    forma_platnosci = models.BooleanField(blank=True,null=True)
    nr_karty = models.CharField(max_length=40)
    termin_karty = models.CharField(max_length=40) 
    nr_seryjny = models.CharField(max_length=40)