from django.db import models
from django.utils.translation import ugettext_lazy as _


class TeamMember(models.Model):
    """
    Entity represents a team member
    """
    name = models.CharField(
        verbose_name=_('name'),
        max_length=20,
        help_text='Enter field documentation'
    )

    deesignation = models.CharField(
        verbose_name=_("Designation"),
        max_length=50,
        help_text=_("The position of the team member."))

    facebook = models.URLField(
        verbose_name=_("Facebook"),
        blank=True, null=True,
        max_length=50,
        help_text=_("Facebook URL"))

    twitter = models.CharField(
        verbose_name=_("Twitter Handle"),
        max_length=50,
        help_text=_("Twitter handle- without `@`."))

    # Metadata
    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    # Methods

    def __str__(self):
        return self.name
