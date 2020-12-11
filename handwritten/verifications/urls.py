"""Signature URLs"""

#Django
from django.urls import path,include

#Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import verifications as verify_views

app_name = 'verify'

router = DefaultRouter()
router.register(r'',verify_views.VerifyViewSet, basename='verify')

urlpatterns=[
    path('',include(router.urls)),    
]