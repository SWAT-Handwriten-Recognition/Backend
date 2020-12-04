#Django
from django.db import models
#Utilities
from handwritten.utils.models import HandwrittenModel
#Model User
from handwritten.users.models import User

class Signature(models.Model):
    """
    This model for save the all signature that included:
        + Username (ForeignKey to User)
        + Image
     
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='signature/pictures')