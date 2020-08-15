from decimal import Decimal as D

from oscar.apps.shipping.repository import Repository as CoreRepository
from oscar.apps.shipping.methods import Free

from gs_shipping.models import ShippingMethod

from apps.shipping.methods import GSFree, GSFixedPrice


class Repository(CoreRepository):
    """
    This class is included so that there is a choice of shipping methods.
    Oscar's default behaviour is to only have one which means you can't test
    the shipping features of PayPal.
    """

    def get_available_shipping_methods(
            self, basket, shipping_addr=None, **kwargs):
        """
        Return a list of all applicable shipping method instances for a given
        basket, address etc. This method is intended to be overridden.
        """
        # customize for addresss , location
        # as we have basket object here.
        shipping_methods = ShippingMethod.objects.values('code',
                                                         'name',
                                                         'charge_excl_tax',
                                                         'charge_incl_tax')
        if not shipping_methods:
            return self.methods
        return [GSFixedPrice(**method) for method in shipping_methods]
