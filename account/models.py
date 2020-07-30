from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from VEGS_V1 import settings

GENDER = (
    ('male', _('Man')),
    ('female', _('Woman'))
)

FOOD_TYPE = (
    ('vegeterian', _('Vegetarian')),
    ('vegan', _('Vegan')),
    ('raw_foodist', _('Raw foodist')),
    ('I_strive', _('I stirve')),
)


class VegsUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = VegsUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE, db_index=True)

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    is_online = models.BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)
    about = models.TextField(max_length=300, blank=True)
    town = models.CharField(max_length=30, blank=True)

    @property
    def _id(self):
        return self.user_id

    @property
    def age(self):
        return timezone.now().year - self.birthday.year

    @property
    def full_name(self):
        return '{first} {last}'.format(first=self.first_name, last=self.last_name)

    food_type = models.CharField(
        verbose_name='Food_type',
        choices=FOOD_TYPE,
        db_index=True,
        max_length=12
    )

    gender = models.CharField(
        verbose_name=_('Gender'),
        choices=GENDER,
        db_index=True,
        max_length=6
    )

    def __str__(self):
        return 'Profile of %s' % self.user_id


class UserPreference(models.Model):
    user = models.OneToOneField(User, related_name='user_preference', on_delete=models.CASCADE, db_index=True)

    gender_pref = models.CharField(
        verbose_name=_('Gender'),
        choices=GENDER,
        db_index=True,
        max_length=6
    )

    food_type_pref = models.CharField(
        verbose_name='Food_type',
        choices=FOOD_TYPE,
        db_index=True,
        max_length=12
    )

    age_pref_min = models.IntegerField(blank=True,
                                       choices=[(x, str(x)) for x in range(18, 90)],
                                       default=18)
    age_pref_max = models.IntegerField(blank=True,
                                       choices=[(x, str(x)) for x in range(18, 90)], null=True)
    distance_pref_min = models.IntegerField(blank=True,
                                            choices=[(x, str(x)) for x in range(1, 200)],
                                            default=1)
    distance_pref_max = models.IntegerField(blank=True,
                                            choices=[(x, str(x)) for x in range(1, 200)], null=True)

    def __str__(self):
        return 'Preference of %s' % self.user_id
