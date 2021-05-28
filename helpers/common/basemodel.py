from django.db import models
import uuid
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of an object.")
    )
    created_date = models.DateTimeField(
        verbose_name=_("Created Date"),
        default=timezone.now,
        max_length=20,
        help_text=_("Timestamp when the record was created."))

    modified_date = models.DateTimeField(
        verbose_name=_("Modified Date"),
        default=timezone.now,
        max_length=20,
        help_text=_("Timestamp when the record was modified."))

    # Metadata
    class Meta:
        abstract = True
