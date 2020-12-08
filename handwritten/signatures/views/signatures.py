"""Signature Views"""

#Django REST Framework

from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

# Serializers
from handwritten.signatures.serializers import SignatureModelSerializer

#Model
from handwritten.signatures.models import Signature


class SignatureViewSet(viewsets.ModelViewSet):

    
    serializer_class = SignatureModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):              
        return Signature.objects.filter(username_id=self.request.data['username'])
