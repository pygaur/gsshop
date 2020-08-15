"""
"""

from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from oscar.core.loading import get_model

from .forms import CODForm
from gs_payment import gateway
from oscar.apps.payment.forms import BillingAddressForm

Source = get_model("payment", "Source")
SourceType = get_model("payment", "SourceType")


class PaymentDetailsView(CorePaymentDetailsView):
    """
    """
    template_name = 'oscar/checkout/payment_details.html'
    template_name_preview = 'oscar/checkout/preview.html'

    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
        'check_user_email_is_captured',
        'check_shipping_data_is_captured',
        'check_payment_data_is_captured']

    def get_context_data(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        if 'cod_form' not in kwargs:
            ctx['cod_form'] = CODForm()
        ctx['billing_address_form'] = kwargs.get(
            'billing_address_form', BillingAddressForm())
        return ctx

    def handle_payment_details_submission(self, request):
        cod_form = CODForm(request.POST)
        if cod_form.is_valid():
            return self.render_preview(request)
        return self.render_payment_details(request, cod_form=cod_form)

    def get_pre_conditions(self, request):
        if self.preview:
            # The preview view needs to ensure payment information has been
            # correctly captured.
            return self.pre_conditions + ['check_payment_data_is_captured']
        return super().get_pre_conditions(request)

    def handle_payment(self, order_number, total, **kwargs):
        """
        :param order_number:
        :param total:
        :param kwargs:
        :return:
        """
        reference = gateway.create_transaction(order_number, total)

        source_type, is_created = SourceType.objects.get_or_create(
            name='Cash on Delivery')
        source = source_type.sources.model(
            source_type=source_type,
            currency=total.currency,
            amount_allocated=total.incl_tax
        )
        self.add_payment_source(source)
        self.add_payment_event('Authorised', total.incl_tax,
                               reference=reference)

