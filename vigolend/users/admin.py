
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# from vigolend.users.forms import UserChangeForm, UserCreationForm
from .models import UserAddress
User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country_of_residence')
    list_display_links = ('first_name', 'last_name', 'country_of_residence')


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line_1', 'address_line_2', 'state', 'city', 'zip_post_code', 'country')

    list_display_links = ('user', 'address_line_1', 'address_line_2', 'state', 'city', 'zip_post_code', 'country')
