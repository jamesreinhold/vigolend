import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class User(AbstractUser):
    """Default user for VigoLend."""

    # USER CHOICES
    KYC_STATUS = (
        ('unverified', _('Unverifed')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action Required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )
    #: First and last name do not cover name patterns around the globe
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)

    # username = None

    first_name = models.CharField(
        max_length=255,
        verbose_name=_("First names"),
        blank=True, null=True,
        help_text=_("The first names of the customer.")
    )

    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Last names"),
        blank=True, null=True,
        help_text=_("The first names of the customer.")
    )

    current_address = models.CharField(
        max_length=255,
        verbose_name=_("Current Address"),
        blank=True, null=True,
        help_text=_("The current living address of the customer.")
    )

    permanent_address = models.CharField(
        max_length=255,
        verbose_name=_("Permanent Address"),
        blank=True, null=True,
        help_text=_("The permanent address of the customer.")
    )

    contact_number = models.CharField(
        max_length=50,
        verbose_name=_("Contact Number"),
        blank=True, null=True,
        help_text=_("The contact number of the customer.")
    )

    date_of_birth = models.DateField(
        verbose_name=_("Date of Birth"),
        blank=True, null=True,
        help_text=_("The birth date of the customer.")
    )

    kyc_complete = models.BooleanField(
        verbose_name=_("KYC Complete"),
        default=False,
        help_text=_("Flag to determine if customer has completed KYC verification.")
    )

    kyc_complete_date = models.DateTimeField(
        verbose_name=_("KYC Complete Date"),
        blank=True, null=True,
        help_text=_("Timestamp when customer completed KYC verification process.")
    )

    kyc_status = models.CharField(
        verbose_name=_("KYC Status"),
        choices=KYC_STATUS,
        default='Unverified',
        blank=True, null=True,
        max_length=15,
        help_text=_("The KYC Status of the customer.")
    )

    on_boarding_complete = models.BooleanField(
        verbose_name=_("Completed Onboarding"),
        default=False,
        help_text=_("Flag to determine if customer has completed onboarding process.")
    )

    on_boarding_complete_date = models.DateTimeField(
        verbose_name=_("Onboarding Complete Date"),
        blank=True, null=True,
        help_text=_("Timestamp when customer completed onboarding process.")
        )

    kyc_submitted = models.BooleanField(
        verbose_name=_("KYC Submitted"),
        default=False,
        help_text=_("Flag to determine if customer has submitted a KYC Verification."))

    social_security_number = models.CharField(
        verbose_name=_("Social Security Number"),
        max_length=50,
        blank=True, null=True,
        help_text=_("The social security number of the customer. This helps to determine the credit score and also validates the identity of the customer.")
        )

    place_of_birth = models.CharField(
        max_length=150,
        verbose_name=_("Place of Birth"),
        blank=True, null=True,
        help_text=_("The place of birth of the customer. This must match the place of birth as indicated in the customers photo Identitication.")
    )

    verification_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Verification Date"),
        blank=True, null=True,
        editable=False,
        help_text=_("Timestamp when customers profile was verified.")
    )

    registered_ip_address = models.GenericIPAddressField(
        verbose_name=_("Registered IP Address"),
        blank=True, null=True,
        editable=False,
        help_text=_("The IP address recorded at the time of registration.")
    )

    country_of_residence = models.CharField(
         max_length=150,
        verbose_name=_("Country of Residence"),
        blank=True, null=True,
        help_text=_("The country of residence of the customer. KYC Verification will be applied to this country and customer must provide proof of such residence as relevant in the country of jurisdiction.")
    )

    default_currency = models.CharField(
        max_length=3,
        verbose_name=_("Default Currency"),
        default='EUR',
        blank=True, null=True,
        help_text=_("The default currency of the borrower. Currency will be sent against borrowers country of residence.")
    )

    job_title= models.CharField(
        max_length=150,
        verbose_name=_("Job Title"),
        blank=True, null=True,
        help_text=_("The job title of the customer.")
    )

    # pending_cash_balance
    # time_zone
    # salutation
    # highest_qualification
    # passout_year
    # investment_limit
    # fund_committed
    # escrow_account_number
    # tax_id


    class Meta:
        verbose_name = _("Register User")
        verbose_name_plural = _("Registered Users")


    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.pk})
