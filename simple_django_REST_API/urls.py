"""
Definition of urls for simple_django_REST_API.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', include('api.urls'))



]