from django.contrib import admin


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso2', 'created_date', 'modified_date')
    list_display_links = ('name', 'iso2', 'created_date', 'modified_date')


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso2', 'country_code', 'created_date', 'modified_date')
    list_display_links = ('name', 'iso2', 'country_code', 'created_date', 'modified_date')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_code', 'state_code', 'created_date', 'modified_date')
    list_display_links = ('name', 'country_code', 'state_code', 'created_date', 'modified_date')
