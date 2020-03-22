"""
"""
from django.utils.translation import ugettext_lazy as _
from django.db import models

from oscar.apps.address.abstract_models import AbstractUserAddress

from phonenumber_field.modelfields import PhoneNumberField


OFFICE = 1
HOME = 2

CHOICES = (
    (OFFICE, 'OFFICE'),
    (HOME, 'HOME')
)


class UserAddress(AbstractUserAddress):
    """
    """
    email = models.EmailField(_("Email ID"), blank=True, help_text=_("Email Address"))
    alt_phone_number = PhoneNumberField(
        _("Alternate Phone number"), blank=True,
        help_text=_("Alternate Contact Number"))
    address_type = models.IntegerField(choices=CHOICES, default=HOME)

    def clean(self):
        # Strip all whitespace
        for field in ['first_name', 'line1', 'line2', 'line3',
                      'line4', 'state', 'postcode']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

        # Ensure postcodes are valid for country
        self.ensure_postcode_is_valid_for_country()

    def _update_search_text(self):
        search_fields = filter(
            bool, [self.first_name,
                   self.line1, self.line2, self.line3, self.line4,
                   self.state, self.postcode, self.country.name])
        self.search_text = ' '.join(search_fields)

    # PROPERTIES

    @property
    def address(self):
        return self.line1

    @property
    def locality(self):
        return self.line2

    @property
    def landmark(self):
        return self.line3

    # city already defined in parent class

    @property
    def pincode(self):
        return self.postcode

    @property
    def salutation(self):
        return self.join_fields(
            ('title', 'first_name'),
            separator=u" ")

    # as first_name is of 255 char so using it.
    @property
    def name(self):
        return self.first_name

from oscar.apps.address.models import *  # noqa isort:skip
