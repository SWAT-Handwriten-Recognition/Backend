"""Signature Serializer."""

#Django REST Framework
from rest_framework import serializers

#Model
from handwritten.signatures.models import Signature

class SignatureModelSerializer(serializers.ModelSerializer):
    """Circle model serializer"""
    class Meta:
        """Meta Class"""
        model = Signature
        fields = (
            'username',
            'picture',
        )

        read_only_fields = (
            'picture',
        )
