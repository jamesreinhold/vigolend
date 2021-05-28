# Django Apps
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    """Represents a country"""
    # region Fields
    name = models.CharField(
        max_length=255,
        verbose_name=_('Country Name'),
        help_text=_('English name of country'))

    phone_code = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name=_('Phone Code'),
        help_text=_('Countries International dialing phone code.'))

    currency = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name=_('Currency'),
        help_text=_('Official country currency.'))

    iso2 = models.CharField(
        max_length=2,
        blank=True, null=True,
        verbose_name=_('ISO2'),
        help_text=_('Two-letter country code'))

    native = models.CharField(
        max_length=255,
        blank=True, null=True,
        help_text=_('Localized or native language of country.'))

    created_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Created Date'),
        help_text=_('Timestamp when the record was created'))

    modified_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Modified Date'),
        help_text=_('Timestamp when the record was modified.'))

    accept_signup = models.BooleanField(
        default=True,
        verbose_name=_('Accept Registration'),
        help_text=_('Allow users from country to register.'))

    banned = models.BooleanField(
        default=False,
        verbose_name=_('Banned'),
        help_text=_('Indicate if country is banned or not'))
    # endregion

    # region Metadata
    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        db_table = 'countries'
    # endregion

    # region Methods
    def __str__(self):
        return self.name
    # endregion


class State(models.Model):
    """Represents countries States and Regions"""
    # region Fields
    name = models.CharField(
        max_length=255,
        verbose_name=_('State Name'),
        help_text=_('The name of the State or Region.'))

    country_code = models.CharField(
        max_length=2,
        blank=True,
        verbose_name=_('Country Code'),
        help_text=_('The ISO 4217 code of the Country.'))

    iso2 = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name=_('ISO2'),
        help_text=_('Two-letter state code'))

    created_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Created Date'),
        help_text=_('Timestamp when the record was created'))

    modified_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Modified Date'),
        help_text=_('Timestamp when the record was modified.'))

    # endregion

    # region Navigation Fields
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_('Country Name'),
        help_text=_('Name of the country of the State or Provinces.'))

    # endregion

    # region Metadata
    class Meta:
        verbose_name = _("State / Region")
        verbose_name_plural = _("States & Regions")
        db_table = 'state_regions'
    # endregion

    # region Methods
    def __str__(self):
        return self.name
    # endregion


class City(models.Model):
    """Represents Cities and Location data of countries around the world"""
    # region Fields
    name = models.CharField(
        max_length=255,
        verbose_name=_('City Name'),
        help_text=_(' The name of the city location.'))

    country_code = models.CharField(
        max_length=5,
        blank=True,
        verbose_name=_('Country Code'))

    state_code = models.CharField(
        max_length=5,
        blank=True, null=True,
        verbose_name=_('State Code'))

    created_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Created Date'),
        help_text=_('Timestamp when the record was created.'))

    modified_date = models.DateTimeField(
        default=timezone.now,
        blank=True, editable=False,
        verbose_name=_('Modified Date'),
        help_text=_('Timestamp when the record was modified.'))

    # endregion

    # region Navigation Fields
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_('Country Name'),
        help_text=_('Name of the country of the State or Provinces.'))

    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        verbose_name=_('State'),
        help_text=_('The name of the State or Provinces. Identifies a subdivision of a country such as state, region, county.'))
    # endregion

    # region Metadata
    class Meta:
        verbose_name = _("City Location")
        verbose_name_plural = _("City Locations")
        db_table = 'city_locations'
    # endregion

    # region Methods
    def __str__(self):
        return self.name
    # endregion
