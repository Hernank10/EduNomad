from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecursoEducativoViewSet, CursoViewSet

app_name = 'core'

router = DefaultRouter()
router.register(r'recursos', RecursoEducativoViewSet, basename='recurso')
router.register(r'cursos', CursoViewSet, basename='curso')

urlpatterns = [
    path('', include(router.urls)),
]
