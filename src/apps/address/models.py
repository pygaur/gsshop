"""
"""
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core import exceptions

from oscar.apps.address.abstract_models import AbstractUserAddress

from phonenumber_field.modelfields import PhoneNumberField


OFFICE = '1'
HOME = '2'

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
    address_type = models.CharField(max_length=1,
                                    choices=CHOICES, default=HOME)

    # Fields, used for `summary` property definition and hash generation.
    base_fields = hash_fields = ['salutation', 'address_type', 'line1', 'line2',
                                 'line3', 'line4', 'state', 'postcode', 'country']

    def get_field_values(self, fields):
        field_values = []
        for field in fields:
            # Title is special case
            if field == 'title':
                value = self.get_title_display()
            elif field == 'address_type':
                value = self.get_address_type_display()
            elif field == 'country':
                try:
                    value = self.country.printable_name
                except exceptions.ObjectDoesNotExist:
                    value = ''
            elif field == 'salutation':
                value = self.salutation
            else:
                value = getattr(self, field)
            field_values.append(value)
        return field_values

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
            bool, [self.first_name, self.address_type,
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

    # city already defined in parent class as line4

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
