import math

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from rest_framework.authtoken.models import Token

from core.models import SoftDeleteModel, TimeStampedModel, UserTimeStampedModel
from core.constants import *


class AppUserManager(BaseUserManager):
    use_in_migrations = True

    # def _create_user(self, username, email, password, **extra_fields):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        # if not username:
        #     raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # username = self.model.normalize_username(username)
        # user = self.model(username=username, email=email, **extra_fields)
        print('extra_fields:// auth/models:// ', extra_fields)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_staff(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, SoftDeleteModel, UserTimeStampedModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    # last_name = models.CharField(_('last name'), max_length=150, blank=True, null=True)
    full_name = models.CharField(_('full name'), max_length=150, blank=True, null=True)
    # email = models.EmailField(_('email address'), blank=True)
    email = models.EmailField(_('email address'), unique=True)
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
    # joined_at = models.DateTimeField(_('date joined'), default=timezone.now)
    # updated_at = models.DateTimeField(blank=True, null=True, verbose_name='updated at', editable=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # def get_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     first_name = self.first_name
    #     last_name = self.last_name
    #     if not first_name and not last_name:
    #         return
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # @property
    # def token(self):
    #     """
    #     Allows us to get a user's token by calling `user.token`.
    #
    #     The `@property` decorator above makes this possible. `token` is called
    #     a "dynamic property".
    #     """
    #
    #     token = Token.objects.get_or_create(user=self)[0]
    #     token = token.key
    #     if token:
    #         # Return our key for consumption.
    #         return token
    #     return None

    @property
    def percentage_complete(self):
        """
        Allows us to get a user's token by calling `user.token`.

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """

        total = 0
        if self.email:
            total += self.__weighted_percentile(weight_for=WEIGHT_EMAIL)
        if self.is_active:
            total += self.__weighted_percentile(weight_for=WEIGHT_IS_ACTIVE)
        if self.username:
            total += self.__weighted_percentile(weight_for=WEIGHT_USERNAME)
        if self.profile.avatar:
            total += self.__weighted_percentile(weight_for=WEIGHT_AVATAR)
        if self.profile.bio:
            total += self.__weighted_percentile(weight_for=WEIGHT_BIO)
        if self.full_name:
            total += self.__weighted_percentile(weight_for=WEIGHT_FULL_NAME)
        # if self.last_name:
        #     total += self.__weighted_percentile(weight_for=WEIGHT_LAST_NAME)

        # and so on
        return "%s" % total

    @staticmethod
    def __weighted_percentile(weight_for):
        weights = WEIGHT_DISTRIBUTIONS
        total_weight = sum(weights.values())
        share = math.floor((weights.get(weight_for, 0) / total_weight) * 100)
        return share
