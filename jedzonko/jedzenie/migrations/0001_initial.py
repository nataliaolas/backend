# Generated by Django 3.1.2 on 2020-10-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pozycja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.FloatField()),
                ('nazwa', models.CharField(max_length=50)),
                ('sklad', models.TextField()),
            ],
        ),
    ]
