from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum
from .models import RecursoEducativo, Curso
from .serializers import (
    RecursoEducativoSerializer, RecursoEducativoSimpleSerializer,
    CursoSerializer, CursoSimpleSerializer
)

def home(request):
    """Vista principal - Dashboard"""
    recursos = RecursoEducativo.objects.all()
    cursos = Curso.objects.all().order_by('-id')[:10]
    
    total_recursos = recursos.count()
    total_cursos = cursos.count()
    total_categorias = recursos.values('categoria').distinct().count()
    total_bytes = recursos.aggregate(Sum('tamanio_bytes'))['tamanio_bytes__sum'] or 0
    total_mb = round(total_bytes / (1024 * 1024), 1)
    
    context = {
        'total_recursos': total_recursos,
        'total_cursos': total_cursos,
        'total_categorias': total_categorias,
        'total_mb': total_mb,
        'cursos': cursos,
        'recursos': recursos,
    }
    return render(request, 'lms/home.html', context)

def explorar_recursos(request):
    """Vista para explorar recursos educativos"""
    recursos = RecursoEducativo.objects.all().order_by('-id')
    categorias = RecursoEducativo.objects.values_list('categoria', flat=True).distinct()
    
    context = {
        'recursos': recursos,
        'categorias': categorias,
        'total_recursos': recursos.count(),
    }
    return render(request, 'lms/explorar_recursos.html', context)

def lista_cursos(request):
    """Vista para listar todos los cursos"""
    cursos = Curso.objects.all().order_by('-fecha_creacion')
    
    # Calcular total de recursos por curso (usando annotate)
    cursos = cursos.annotate(total_recursos_count=Count('recursos'))
    
    context = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, 'lms/cursos/lista.html', context)

def detalle_curso(request, curso_id):
    """Vista para ver detalle de un curso"""
    curso = get_object_or_404(Curso, id=curso_id)
    
    # Obtener recursos del curso
    recursos = curso.recursos.all()
    
    # Intentar obtener lecciones (desde language_practice)
    try:
        from apps.language_practice.models import Course, Lesson
        course_lp = Course.objects.filter(title=curso.titulo).first()
        lecciones = Lesson.objects.filter(course=course_lp).order_by('order') if course_lp else []
    except:
        lecciones = []
    
    context = {
        'curso': curso,
        'recursos': recursos,
        'lecciones': lecciones,
        'total_recursos': recursos.count(),
        'total_lecciones': len(lecciones),
    }
    return render(request, 'lms/cursos/detalle.html', context)


# API Views
class RecursoEducativoViewSet(viewsets.ModelViewSet):
    queryset = RecursoEducativo.objects.all()
    serializer_class = RecursoEducativoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre_archivo', 'categoria', 'descripcion', 'etiquetas']
    ordering_fields = ['nombre_archivo', 'categoria', 'tamanio_bytes', 'fecha_creacion']
    ordering = ['categoria', 'nombre_archivo']
    
    @action(detail=False, methods=['get'])
    def categorias(self, request):
        categorias = RecursoEducativo.objects.values('categoria').annotate(
            cantidad=Count('id')
        ).order_by('-cantidad')
        
        total = RecursoEducativo.objects.count()
        for cat in categorias:
            cat['porcentaje'] = round(cat['cantidad'] / total * 100, 1) if total > 0 else 0
        
        return Response(categorias)
    
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        total = RecursoEducativo.objects.count()
        total_bytes = RecursoEducativo.objects.aggregate(
            total_bytes=Sum('tamanio_bytes')
        )['total_bytes'] or 0
        
        categorias = RecursoEducativo.objects.values('categoria').annotate(
            cantidad=Count('id')
        ).order_by('-cantidad')
        
        return Response({
            'total_archivos': total,
            'total_mb': round(total_bytes / (1024 * 1024), 2),
            'categorias': categorias,
        })


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descripcion', 'categoria', 'palabras_clave']
    ordering_fields = ['titulo', 'categoria', 'nivel', 'duracion_horas', 'precio', 'fecha_creacion']
    ordering = ['-fecha_creacion']
    
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        total = Curso.objects.count()
        publicados = Curso.objects.filter(estado='PUBLICADO').count()
        
        return Response({
            'total_cursos': total,
            'cursos_publicados': publicados,
        })

def detalle_practica(request, practica_id):
    """Vista para ver una práctica interactiva"""
    from .models import Practica, EjercicioInteractivo
    
    practica = get_object_or_404(Practica, id=practica_id, is_active=True)
    ejercicios = EjercicioInteractivo.objects.filter(practica=practica, is_active=True).order_by('orden')
    
    context = {
        'practica': practica,
        'ejercicios': ejercicios,
        'total_ejercicios': ejercicios.count(),
    }
    return render(request, 'lms/practicas/detalle.html', context)

def detalle_evaluacion(request, evaluacion_id):
    """Vista para ver una evaluación"""
    from .models import Evaluacion, EjercicioInteractivo
    
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id, is_active=True)
    ejercicios = EjercicioInteractivo.objects.filter(evaluacion=evaluacion, is_active=True).order_by('orden')
    
    context = {
        'evaluacion': evaluacion,
        'ejercicios': ejercicios,
        'total_ejercicios': ejercicios.count(),
    }
    return render(request, 'lms/evaluaciones/detalle.html', context)
