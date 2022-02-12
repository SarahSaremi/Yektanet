from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ad_system/', include('ad_system.urls')),
    path('admin/', admin.site.urls),
]
