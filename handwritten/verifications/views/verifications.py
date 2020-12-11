"""Verify Views"""

#Django REST Framework

from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


#Serializer
from handwritten.verifications.serializers import VerifyModelSerializer,AddVerifySerializer


class VerifyViewSet(viewsets.GenericViewSet):

    serializer_class = AddVerifySerializer
    permission_classes = (IsAuthenticated,)    

    @action(detail=False,methods=['post'])
    def verify(self,request):
        serializer = AddVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        verify = serializer.save()
        data = {
            'status':VerifyModelSerializer(verify).data            
        }
        return Response(data, status=status.HTTP_201_CREATED)