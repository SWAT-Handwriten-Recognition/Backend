"""Signature Serializer."""

#Django REST Framework
from rest_framework import serializers

#Model
from handwritten.signatures.models import Signature
from handwritten.users.models import User

class SignatureModelSerializer(serializers.ModelSerializer):
    """Signature model serializer"""
    class Meta:
        """Meta Class"""
        model = Signature
        fields = (
            'username',
            'picture',
        )

class AddSignatureModelSerializer(serializers.Serializer):
    """Model Serializer to Create a new Signature"""
    username = serializers.CharField()
    picture = serializers.ImageField()

    def create(self,data):
        user = User.objects.get(username=data['username'])    
        Signature = Signature.objects.create(username=user,picture=data['picture'])
        return Signature
