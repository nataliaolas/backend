# Generated by Django 3.1.1 on 2021-01-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzenie', '0014_auto_20210103_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platnosc',
            name='termin_karty',
            field=models.CharField(max_length=40),
        ),
    ]
