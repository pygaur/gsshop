"""
"""
from django.forms import Form
from oscar.apps.checkout.forms import ShippingAddressForm
from oscar.core.loading import get_model

#from captcha.fields import CaptchaField


class ShippingAddressForm(ShippingAddressForm):
    """
    Custom Shipping Address form
    """

    def __init__(self, *args, **kwargs):
        # phone_number in database is blank=True
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True

    class Meta:
        model = get_model('order', 'shippingaddress')
        fields = [
            'first_name',
            "phone_number",
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode', 'country',
            'address_type'
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


#class CODForm(Form):
#    """
#    cash on delivery form to display captcha.
#    """
#    captcha = CaptchaField()
