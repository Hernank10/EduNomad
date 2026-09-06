from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_api(request):
    return JsonResponse({
        "status": "online",
        "project": "EduNomad API",
        "endpoints": {
            "recursos": "/api/recursos/",
            "cursos": "/api/cursos/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', home_api, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
]
