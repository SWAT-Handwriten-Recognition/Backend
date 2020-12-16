"""Verify Serializer."""
#Request
import requests
import json
#Django REST Framework
from rest_framework import serializers

#Var
from config.settings.base import MEDIA_URL as MEDIA_URL_LOCAL, MEDIA_ROOT as MEDIA_ROOT_LOCAL, PROD as PROD_LOCAL
from config.settings.production import MEDIA_URL as MEDIA_URL_PROD, MEDIA_ROOT as MEDIA_ROOT_PROD, PROD as PROD_PROD
# from config.settings.production import PROD as PROD_PROD
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
        signatures = Signature.objects.filter(username_id=data['username'])[0]
        
        url = "http://ec2-50-19-136-30.compute-1.amazonaws.com:8080/verify"
        if PROD_PROD:        
            
            payload={
                 "database_image":f'{MEDIA_URL_PROD}{signatures.picture.__str__()}',
                 "frontend_image":f'{MEDIA_URL_PROD}{verify.picture.__str__()}'
            }
            # print(payload)
            headers = {
                 'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
            verify.validation_range=float(response['result'])

        # if True:        
            
        #     payload={
        #          "database_image":f'https://signaturestore2.s3.amazonaws.com/signatures/Pedro2/057d1658-3970-11eb-9f95-0242ac120003.jpeg',
        #          "frontend_image":f'https://signaturestore2.s3.amazonaws.com/verifications/Pedro2/955e3e98-3fcc-11eb-afc6-0242ac120003.png'
        #     }
        #     # print(payload)
        #     headers = {
        #          'Content-Type': 'application/json'
        #     }

        #     response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
        #     print(response)
        #     verify.validation_range=float(response['result'])    
        
        
        return verify