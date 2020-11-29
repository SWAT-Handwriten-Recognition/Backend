"""User URLs"""

#Django

from django.urls import path

#Views

from handwritten.users.views import UserLoginAPIView, UserSignUpAPIView

app_name = 'users'

urlpatterns=[
    path('users/login/',UserLoginAPIView.as_view(), name='login'),
    path('users/signup/',UserSignUpAPIView.as_view(), name='signup')
]