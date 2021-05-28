from django.contrib import admin
from .models import City, Country, State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso2', 'created_date', 'modified_date')
    list_display_links = ('name', 'iso2', 'created_date', 'modified_date')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso2', 'country_code', 'created_date', 'modified_date')
    list_display_links = ('name', 'iso2', 'country_code', 'created_date', 'modified_date')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_code', 'state_code', 'created_date', 'modified_date')
    list_display_links = ('name', 'country_code', 'state_code', 'created_date', 'modified_date')
