

from django.db import models
from django.contrib.auth.models import AbstractUser

from handwritten.utils.models import HandwrittenModel

class User(HandwrittenModel,AbstractUser):
    """
    User Model
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            "unique":"The User already exists"
        },
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']

    def __str__(self):
        return self.first_name


    