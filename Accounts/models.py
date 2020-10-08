import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, university, department, batch,year,semester):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email), university=university, department=department ,batch=batch, year=year, semester=semester)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, university, department, semester, batch,year):
        """Create and saves a new user"""
        user = self.create_user(username, email, password, university, department, batch,year, semester)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


    def create_admin(self, username, email, password, university, department=False ,batch=False,year=False,semester=False):
     
        user = self.create_user(username, email ,password, university, department , batch,year, semester)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        
        return user
    """
    def create_admin(self, username, email, password, university):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = User(username=username, email=self.normalize_email(email), university=university)
        user.set_password(password)
        user.is_admin = True
        user.save()
       
       # profile = Profile(
        #    owner=user,
        #    university=university
        #)
       # profile.save()
       #return user
       """

    def create_chairman(self, username, email, password, university, department ,batch=False,year=False, semester=False):
        """Create and saves a new user"""
        user = self.create_user( username, email, password, university, department ,batch,year, semester)
        user.is_chairman = True
        user.save(using=self._db)

        return user

    def create_depHead(self, username, email, password, university, department ,batch=False,year=False, semester=False):
        """Create and saves a new user"""
        user = self.create_user( username, email, password, university, department ,batch, year,  semester)
        user.is_depHead = True
        user.save(using=self._db)

        return user

    def create_teacher(self, username, email, password, university, department ,batch, year, semester):
        """Create and saves a new user"""
        user = self.create_user(username, email, password, university, department ,batch, year, semester)
        user.is_teacher = True
        user.save(using=self._db)

        return user

    def create_student(self, username, email, password, university, department ,batch, year, semester):
        """Create and saves a new user"""
        user = self.create_user(username, email, password, university, department ,batch, year, semester)
        user.is_student = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User models support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    batch = models.CharField(max_length=255 ,default=False , null=True)
    year = models.CharField(max_length=255 ,default=False , null=True)
    semester = models.CharField(max_length=255 ,default=False , null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_chairman = models.BooleanField(default=False)
    is_depHead = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','department']
    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'user': self.username,
            'department': self.department,
            'is_admin': self.is_admin,
            'is_teacher': self.is_teacher,
            'is_student': self.is_student,
            'is_chairman': self.is_chairman,
            'is_depHead': self.is_depHead
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class InventoryFile(models.Model):
    importData = models.FileField(upload_to='inventory/')


class ProfileCheck(models.Model):
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50, blank=True)
    csv_file = models.FileField(upload_to='inventory/', blank=True)

    def __str__(self):
        return self.name

#class Profile(models.Model):
 #   owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
  #  university = models.CharField(max_length=100)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
 #    if created:
  #      Profile.objects.create(user=instance)

#@ receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
 #   instance.profile.save()
