"""
"""
from django.db import transaction

from .models import CashOnDeliveryTransaction


@transaction.atomic
def create_transaction(order_number, total, *args, **kwargs):
    txn = CashOnDeliveryTransaction.objects.get_or_create(
        order_number=order_number,
        amount=total.incl_tax,
        currency=total.currency
    )
    return txn[0].reference
