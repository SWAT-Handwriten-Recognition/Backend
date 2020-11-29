"""User Views"""

#Django REST Framework
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response

#Serializers
from handwritten.users.serializers import ( 
    UserLoginSerializer, 
    UserModelSerializer,
    UserSignUpSerializer
)

class UserLoginAPIView(APIView):
    """User login API view"""
    def post(self,request,*args,**kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'status':UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

class UserSignUpAPIView(APIView):
    """User SignUp API view"""
    def post(self,request,*args,**kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        user = serializer.save()        
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)