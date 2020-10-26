from django.db import models
from django.contrib.auth.models import User

class Pozycja(models.Model):
    cena = models.FloatField()
    nazwa = models.CharField(max_length=50)
    sklad = models.TextField()
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nazwa +" "+ str(self.cena) +" " + self.sklad

class Restauracja(models.Model):
    opis = models.TextField(null=True)
    adresy = models.ManyToManyField('Adres')
    wlasciciel = models.ForeignKey('Wlasciciel', on_delete=models.CASCADE, null=True)


class Adres(models.Model):
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)
    nr_budynku = models.IntegerField()
    nr_mieszkania= models.IntegerField()


class Menu(models.Model):
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE, null=True)


class TypRestauracji(models.Model):
    nazwa = models.CharField(max_length=50)


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


class OpiniaORestauracji(models.Model):
    opis = models.TextField()
    zadowolenie_klienta = models.IntegerField()
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE, null=True)