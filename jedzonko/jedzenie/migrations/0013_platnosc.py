# Generated by Django 3.1.1 on 2020-12-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzenie', '0012_restauracja_typ_restauracji'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platnosc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_platnosci', models.BooleanField()),
                ('nr_karty', models.CharField(max_length=40)),
                ('termin_karty', models.DateField()),
                ('nr_seryjny', models.CharField(max_length=40)),
            ],
        ),
    ]
