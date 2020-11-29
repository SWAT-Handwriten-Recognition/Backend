"""Users Serializers"""
#Django
from django.contrib.auth import authenticate, password_validation
# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

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

class UserSignUpSerializer(serializers.Serializer):
    """User Sign Up serializer"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    #Password
    password = serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8,max_length=64)
    #Name
    first_name = serializers.CharField(min_length=2,max_length=30)
    last_name = serializers.CharField(min_length=2,max_length=30)

    def validate(self,data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError('Passwords does not match')
        password_validation.validate_password(passwd)
        return data
    def create(self,data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)        
        return user

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