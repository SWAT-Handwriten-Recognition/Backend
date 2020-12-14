"""Signature Views"""

#Django REST Framework

from rest_framework import status,viewsets, generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

#Filter
from rest_framework.filters import SearchFilter

# Serializers
from handwritten.signatures.serializers import SignatureModelSerializer, AddSignatureModelSerializer

#Model
from handwritten.signatures.models import Signature

# class SignatureViewSet(viewsets.GenericViewSet):

#     serializer_class = AddSignatureModelSerializer
#     permission_classes = (IsAuthenticated,)    

#     @action(detail=False,methods=['post'])
#     def signatures(self,request):
#         serializer = AddSignatureModelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         signature = serializer.save()
#         data = {
#             'status': status.HTTP_201_CREATED,
#             'data':  SignatureModelSerializer(signature).data          
#         }
#         return Response(data, status=status.HTTP_201_CREATED)
    
    # def get_queryset(self):
    #     """Return circle members."""
    #     username = self.kwargs['username']
    #     return Signature.objects.filter(
    #         username_id=username
    #     )

    # @action(detail=True,methods=['get'])
    # def signatures(self,request):
    #     username = self.kwargs['username']
    #     signature = Signature.objects.filter(username_id=self.request.data['username'])        
    #     data = {
    #         'status': status.HTTP_200_OK,
    #         'data':  SignatureModelSerializer(signature).data            
    #     }
    #     return Response(data, status=status.HTTP_200_OK)

# class SignatureList(viewsets.GenericViewSet):
    
    
#     serializer_class = SignatureModelSerializer
#     permission_classes = (IsAuthenticated,)  

#     def get_queryset(self):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         """Return circle members."""
#         username=self.kwargs['username']
#         return Signature.objects.filter(
#             username_id=username
#         )

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
