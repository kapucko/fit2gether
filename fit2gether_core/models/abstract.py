import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Fit2getherModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name=_('Last modified'), auto_now=True)


class FromToModel(Fit2getherModel):

    class Meta:
        abstract = True

    date_from = models.DateTimeField(verbose_name=_('Event starts'), blank=True)
    date_to = models.DateTimeField(verbose_name=_('Event ends'), blank=True)

    def clean(self):
        if self.date_from and self.date_to and self.date_from >= self.date_to:
            msg = _('%(date_from)s have to be before %(date_to)s.') % {
                'date_from': self._meta.get_field('date_from').verbose_name,
                'date_to': self._meta.get_field('date_to').verbose_name
            }

        raise ValidationError({'date_from': msg, 'date_to': msg})