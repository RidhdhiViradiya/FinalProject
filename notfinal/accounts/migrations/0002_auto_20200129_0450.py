# Generated by Django 3.0.2 on 2020-01-28 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='area',
            table='Area',
        ),
        migrations.AlterModelTable(
            name='city',
            table='city',
        ),
    ]
