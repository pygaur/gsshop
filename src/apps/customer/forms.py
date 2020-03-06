"""
"""
from oscar.apps.customer.forms import EmailUserCreationForm
from oscar.core.compat import get_user_model

User = get_user_model()


class EmailUserCreationForm(EmailUserCreationForm):

    class Meta:
        """
        """
        model = User
        fields = ('name', 'email', 'phone_number')
