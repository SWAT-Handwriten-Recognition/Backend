"""Users Serializers"""
#Django
from django.contrib.auth import authenticate
# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

#Models
from handwritten.users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""
    class Meta():
        """Meta Class."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


class UserLoginSerializer(serializers.Serializer):
    """ User login Serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self,data):
        """Check credentials"""
        user = authenticate(username=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return data
    def create(self,data):
        """Generate or retrive new tocken"""
        tocken, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], tocken.key