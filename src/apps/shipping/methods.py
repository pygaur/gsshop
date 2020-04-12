from decimal import Decimal as D

from oscar.apps.shipping.methods import Base, Free, FixedPrice
from oscar.core import prices

from django.utils.translation import gettext_lazy as _


class GSFree(Free):
    """
    This shipping method specifies that shipping is free.
    """

    def __init__(self, *args, **kwargs):
        self.code = args[0]
        self.name = args[1]
        super().__init__(*args, **kwargs)


class GSFixedPrice(FixedPrice):
    """
    This shipping method indicates that shipping costs a fixed price and
    requires no special calculation.
    """

    def __init__(self, code=None, name=None,
                 charge_excl_tax=None, charge_incl_tax=None):
        self.code = code
        self.name = name
        super().__init__(charge_excl_tax, charge_incl_tax)

