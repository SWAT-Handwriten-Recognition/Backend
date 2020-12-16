"""Signature Views"""

#Django REST Framework

from rest_framework import status,viewsets, generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

#Filter
from rest_framework.filters import SearchFilter

# Serializers
from handwritten.signatures.serializers import SignatureModelSerializer

#Model
from handwritten.signatures.models import Signature

class SignatureViewSet(viewsets.ModelViewSet):

    
    serializer_class = SignatureModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self): 
        # import ipdb;ipdb.set_trace()   
        queryset = Signature.objects.all()
        username = self.request.query_params.get('username', None)          
        # return Signature.objects.filter(username_id=self.request.data['username'])
        if username is not None:
            queryset = queryset.filter(username_id=username)
        return queryset
