from django.contrib import admin
from django.urls import path, include
from apps.core.views import home, explorar_recursos, detalle_curso
from apps.core.views_auth import (
    register_view, login_view, logout_view, 
    perfil_view, dashboard_estudiante
)

urlpatterns = [
    # Página principal
    path('', home, name='home'),
    
    # Autenticación
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil_view, name='perfil'),
    path('dashboard/', dashboard_estudiante, name='dashboard_estudiante'),
    
    # Recursos y cursos
    path('recursos/', explorar_recursos, name='explorar_recursos'),
    path('cursos/<int:curso_id>/', detalle_curso, name='detalle_curso'),
    
    # Admin y API
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
]
