"""Verify Serializer."""

#Django REST Framework
from rest_framework import serializers

#Model
from handwritten.verifications.models import Verify
from handwritten.signatures.models import Signature
from handwritten.users.models import User

#Model Data Science
# from handwritten.datascience import load

class VerifyModelSerializer(serializers.ModelSerializer):
    """Verify model serializer"""
    class Meta:
        """Meta Class"""
        model = Verify
        fields = (
            'username',
            'validation_range',
        )

class AddVerifySerializer(serializers.Serializer):
    """Verify Selializar"""
    username = serializers.CharField()
    picture = serializers.ImageField()

    def create(self, data): 
        """Created a new validation"""   
        user = User.objects.get(username=data['username'])    
        verify = Verify.objects.create(username=user,picture=data['picture'])
        # verify.save()
        signatures = Signature.objects.filter(username_id=data['username'])
        import ipdb;ipdb.set_trace()
        #Run the Model Science
        
        return verify