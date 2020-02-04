from django.contrib import admin
from django.contrib.auth.models import Area, City, User
from django.core.paginator import Paginator
# # Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    ordering = ['city_name']
    search_fields = ['city_name']
    list_per_page = 15


admin.site.site_header = "'WeCare' Administration"
admin.site.site_title = "Administraion Controls"
admin.site.index_title = "Database Tables"
admin.site.register(Area)
admin.site.register(City, CityAdmin)

