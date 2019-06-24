from django.core.mail import send_mail
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import re


class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        """
        email = self.normalize_email(email)
        """
        user = self.model(username=username, is_staff=is_staff, is_active=True, is_superuser=is_superuser,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=50, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, null=True)
    last_name = models.CharField(_('last name'), max_length=150, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Staff?.'), null=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Ativo?.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), default=timezone.now, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


"""
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
"""
