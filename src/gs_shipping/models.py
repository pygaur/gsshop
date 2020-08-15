"""
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class ShippingMethod(models.Model):
    """
    """
    name = models.CharField(_("Name"), max_length=255,
                            help_text=_("Shipping Method Name"))
    charge_excl_tax = models.DecimalField(max_digits=10, decimal_places=2)
    charge_incl_tax = models.DecimalField(max_digits=10, decimal_places=2)

    code = models.SlugField(unique=True,
                            max_length=255)
    #is_deleted = models.NullBooleanField()

    def save(self, *args, **kwargs):
        self.code = slugify(self.name)
        super(ShippingMethod, self).save(*args, **kwargs)

    class Meta:
        app_label = 'gs_shipping'
        verbose_name = _("Shipping Method")
        verbose_name_plural = _("Shipping Methods")
