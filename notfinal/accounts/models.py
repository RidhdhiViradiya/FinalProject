from django.db import models
from django.contrib.auth.models import User, AbstractUser


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'city'


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=40)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')

    class Meta:
        db_table = 'Area'


class User(AbstractUser):
    USER_TYPES = (
        ("PGVendor", "PGVendor"),
        ("Food Vendor", "Food Vendor"),
        ("Student", "Student")
    )
    user_address = models.CharField(max_length=200, default="")
    user_type = models.CharField(max_length=30, choices=USER_TYPES, blank=True)
    user_phone = models.CharField(max_length=10, blank=True)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE, db_column='area_id', blank=True, null=True)

