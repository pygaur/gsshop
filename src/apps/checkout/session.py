"""
"""
from oscar.apps.checkout.session import  CheckoutSessionMixin as CoreCheckoutSessionMixin


class CheckoutSessionMixin(CoreCheckoutSessionMixin):
    """
    """
    def check_payment_data_is_captured(self, request):
        # We don't collect payment data by default so we don't have anything to
        # validate here. If your shop requires forms to be submitted on the
        # payment details page, then override this method to check that the
        # relevant data is available. Often just enforcing that the preview
        # view is only accessible from a POST request is sufficient.
        import pdb; pdb.set_trace()
