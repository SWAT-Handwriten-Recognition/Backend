"""Signature URLs"""

#Django
from django.urls import path,include

#Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import signatures as signature_views

app_name = 'signatures'

router = DefaultRouter()
router.register(r'signatures',signature_views.SignatureViewSet, basename='signatures')
urlpatterns=[
    path('',include(router.urls))    
]
