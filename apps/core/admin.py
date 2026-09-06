from django.contrib import admin
from .models import RecursoEducativo, Curso

@admin.register(RecursoEducativo)
class RecursoEducativoAdmin(admin.ModelAdmin):
    list_display = ['nombre_archivo', 'categoria', 'extension', 'tamanio_kb']
    list_filter = ['categoria', 'extension']
    search_fields = ['nombre_archivo', 'categoria', 'descripcion']
    
    def tamanio_kb(self, obj):
        return f"{obj.tamanio_kb:.2f} KB"
    tamanio_kb.short_description = 'Tamaño (KB)'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'nivel', 'estado', 'duracion_horas', 'total_recursos']
    list_filter = ['categoria', 'nivel', 'estado']
    search_fields = ['titulo', 'descripcion', 'palabras_clave']
    prepopulated_fields = {'slug': ('titulo',)}
    filter_horizontal = ['recursos']
    
    def total_recursos(self, obj):
        return obj.recursos.count()
    total_recursos.short_description = '# Recursos'
