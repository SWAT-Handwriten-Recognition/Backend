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


