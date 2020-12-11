"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('',include(('handwritten.users.urls'), namespace='users')),
    path('',include(('handwritten.signatures.urls'), namespace='signatures')),
    path('',include(('handwritten.verifications.urls'), namespace='verifications')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
