# Generated by Django 3.0.2 on 2020-01-29 13:13

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200129_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area_id',
            field=models.ForeignKey(blank=True, db_column='area_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.Area'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('PGVendor', 'PGVendor'), ('Food Vendor', 'Food Vendor'), ('Student', 'Student')], max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]