# Generated by Django 3.0.2 on 2020-01-28 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200129_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='city_id',
            field=models.ForeignKey(db_column='city_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.City'),
        ),
    ]