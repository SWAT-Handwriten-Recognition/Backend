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
    return 'signatures/{0}/{1}'.format(instance.username, str(uuid.uuid1())+'.'+extencion) 

class Signature(models.Model):
    """
    This model for save the all signature that included:
        + Username (ForeignKey to User)
        + Image
     
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=directory_path)



