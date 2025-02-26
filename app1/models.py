from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary_storage.storage import MediaCloudinaryStorage


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(
        null=True,blank=True,upload_to='profile_picture',storage=MediaCloudinaryStorage()
    )

    # Tell Django to use email for authentication
    USERNAME_FIELD = 'email'

    # Make sure 'username' is required for superuser creation
    REQUIRED_FIELDS = ['username']

    username = models.CharField(
        max_length=100,
        blank=True,  # Not required for regular users
        null=True,   # Can be null in the database
        default='',  # Default empty string for username
    )


    def __str__(self):
        return self.email

    # def save(self, *args, **kwargs):
    #     # Ensure password is hashed before saving the user object
    #     if self.pk is None:  # Only hash if this is a new user (not updated)
    #         self.set_password(self.password)  # Hash the password
    #     super().save(*args, **kwargs)

class home(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200,null=True)
    cont = models.TextField(blank=False,null=False)
    def __str__(self):
        return self.title
    




