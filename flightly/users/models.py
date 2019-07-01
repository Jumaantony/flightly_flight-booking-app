import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from django_cryptography.fields import encrypt


def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        ext = filename.split('.')[-1]
        return f'img/{uuid.uuid4()}.{ext}'

class FlightlyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
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


class FlightlyUser(AbstractUser):
    '''FlightlyUser extends AbstractUser:
        extra/modified fields:
            email
        additional modifications
            - Makes email the USERNAME_FIELD
            - Makes username a property that return a concatenation of the first and last name (capitalized)
            - Makes the email field required
            - Changes id field to be of type uuid
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': _("A user with that email address already exists."),
    },)
    photograph = encrypt(models.ImageField(_("Passport Photograph"),
                                           default=f"img/{os.getenv('DEFAULT_CLOUDINARY_IMG_NAME')}",
                                           upload_to=user_directory_path
                                           ))


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = FlightlyUserManager()

    class Meta:
        verbose_name = _('Flightly User')
        verbose_name_plural = _('Flightly Users')

    @property
    def username(self):
        return self.get_full_name()
