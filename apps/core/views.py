from rest_framework import viewsets, filters
from .models import RecursoEducativo, Curso
from .serializers import RecursoEducativoSerializer, CursoSerializer


class RecursoEducativoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar Recursos Educativos.
    """
    queryset = RecursoEducativo.objects.all().order_by('-fecha_creacion')
    serializer_class = RecursoEducativoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre_archivo', 'categoria', 'tipo_contenido', 'descripcion']
    ordering_fields = ['fecha_creacion', 'tamanio_bytes']


class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar Cursos.
    """
    queryset = Curso.objects.all().prefetch_related('recursos').order_by('-fecha_creacion')
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'categoria', 'nivel', 'estado']
    ordering_fields = ['fecha_creacion', 'duracion_horas']
