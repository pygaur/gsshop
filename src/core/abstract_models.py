"""
"""
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models
from django.contrib.auth.validators import UnicodeUsernameValidator

from phonenumber_field.modelfields import PhoneNumberField

from .options import GENDER


class AbstractUser(auth_models.AbstractBaseUser,
                   auth_models.PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    removed first_name, last_name field from default AbstractUser
    phone_number and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(_('email address'))
    phone_number = PhoneNumberField(_("Mobile Number"), unique=True)
    dob = models.DateField(_('Date of Birth'), null=True, blank=True)

    is_mobile_verified = models.NullBooleanField()
    is_email_verified = models.NullBooleanField()

    gender = models.PositiveSmallIntegerField(choices=GENDER.CHOICES,
                                              verbose_name='Gender',
                                              null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = auth_models.UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'phone_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        return self.name.strip()

    def get_short_name(self):
        return self.name.strip()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

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