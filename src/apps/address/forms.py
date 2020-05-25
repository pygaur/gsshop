"""
"""
from oscar.core.loading import get_model
from oscar.apps.address.forms import AbstractAddressForm
from oscar.forms.mixins import PhoneNumberMixin

UserAddress = get_model('address', 'useraddress')


class UserAddressForm(PhoneNumberMixin, AbstractAddressForm):
    """
    """
    class Meta:
        """
        """
        model = UserAddress
        fields = [
            'first_name', 'phone_number', 'postcode',
            'line1', 'line2', 'line3', 'line4',
            'state', 'country', 'address_type',
        ]
        exclude = [
            'title', 'last_name',
            'search_text'
        ]
        labels = {
            "first_name":u"Name",
            "line1": u"Address",
            "line2": u"Locality",
            "line3": u"Landmark",
            "line4": u"City",
            "postcode": u"Pincode",
            "state": u"State",
        }

    def __init__(self, user, *args, **kwargs):
        """
        because it is defined into oscar address model.
        :param user:
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.instance.user = user
