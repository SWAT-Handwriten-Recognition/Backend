#Django
from django.db import models
#Utilities
from handwritten.utils.models import HandwrittenModel
import uuid 
#Model User
from handwritten.users.models import User

def directory_path(instance, filename): 
    
    #Extensión file
    extencion = filename.split('.')
    extencion = extencion[len(extencion)-1]
    # file will be uploaded to MEDIA_ROOT / <id>/<filename> 
    return 'verifications/{0}/{1}'.format(instance.username, str(uuid.uuid1())+'.'+extencion) 

class Verify(HandwrittenModel,models.Model):
    """
    This model save all attempts to validate a signature and that included:
        + Username (ForeignKey to User)
        + Image (New Image diferent to Signature)
        + Validation_range
     
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    validation_range = models.FloatField(null=True)
    picture = models.ImageField(upload_to=directory_path)