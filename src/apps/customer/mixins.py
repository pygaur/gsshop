"""
"""
from django.contrib.sites.shortcuts import get_current_site

from oscar.apps.customer.mixins import RegisterUserMixin
from oscar.core.loading import get_class, get_model
from oscar.core.compat import get_user_model

from core.celery import app as celery_app

User = get_user_model()

CommunicationEventType = get_model('customer', 'CommunicationEventType')
Dispatcher = get_class('customer.utils', 'Dispatcher')


@celery_app.task
def send_email(messages, user_id):
    """
    """
    try:
        user = User.objects.get(pk=user_id)
    except User.ObjectDoesNotExist:
        user = None

    if messages and messages['body']:
        Dispatcher().dispatch_user_messages(user, messages)


class RegisterUserMixin(RegisterUserMixin):
    """
    """

    def send_registration_email(self, user):
        code = self.communication_type_code
        site = get_current_site(self.request)
        ctx = {'user': user, 'site': site}
        messages = CommunicationEventType.objects.get_and_render(code, ctx)

        send_email.delay(messages, user.id)

