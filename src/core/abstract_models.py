"""
"""
from django.contrib.auth import models as auth_models
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from oscar.apps.customer.abstract_models import UserManager

from phonenumber_field.modelfields import PhoneNumberField


class GENDER(models.TextChoices):
    MALE = "MALE", "MALE"
    FEMALE = "FEMALE", "FEMALE"


class AbstractUser(auth_models.AbstractBaseUser,
                   auth_models.PermissionsMixin):
    """
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField(_("Mobile Number"),
                                    unique=True,
                                    validators=[])
    dob = models.DateField(_('Date of Birth'), null=True, blank=True)

    is_mobile_verified = models.NullBooleanField()
    is_email_verified = models.NullBooleanField()

    gender = models.CharField(
        _("Gender"), max_length=10, choices=GENDER.choices, default=GENDER.MALE
    )

    is_staff = models.BooleanField(
        _('Staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('Active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'),
                                       default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    class Meta:
        abstract = True
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        """
        return self.name

    def get_short_name(self):
        """
        """
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def _migrate_alerts_to_user(self):
        """
        Transfer any active alerts linked to a user's email address to the
        newly registered user.
        """
        ProductAlert = self.alerts.model
        alerts = ProductAlert.objects.filter(
            email=self.email, status=ProductAlert.ACTIVE)
        alerts.update(user=self, key='', email='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Migrate any "anonymous" product alerts to the registered user
        # Ideally, this would be done via a post-save signal. But we can't
        # use get_user_model to wire up signals to custom user models
        # see Oscar ticket #1127, Django ticket #19218
        self._migrate_alerts_to_user()
