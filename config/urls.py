from django.contrib import admin
from django.urls import path, include
from apps.core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cursos/', include('apps.language_practice.urls')),
    path('generator/', include('apps.generator.urls')),
]
