
from django.contrib import admin

from .models import KycApplication


@admin.register(KycApplication)
class KycApplicationAdmin(admin.ModelAdmin):
    pass
