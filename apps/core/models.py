from django.db import models
from django.utils.text import slugify

class RecursoEducativo(models.Model):
    nombre_archivo = models.CharField(max_length=500)
    ruta_completa = models.CharField(max_length=1000, unique=True)
    extension = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=100, db_index=True)
    tipo_contenido = models.CharField(max_length=50, blank=True, null=True)
    tamanio_bytes = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)
    etiquetas = models.TextField(blank=True, null=True)
    importado_el = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['categoria', 'nombre_archivo']
        indexes = [
            models.Index(fields=['categoria']),
            models.Index(fields=['nombre_archivo']),
        ]
    
    def __str__(self):
        return f"{self.categoria}: {self.nombre_archivo[:50]}"
    
    @property
    def tamanio_kb(self):
        return round(self.tamanio_bytes / 1024, 2)
    
    @property
    def tamanio_mb(self):
        return round(self.tamanio_bytes / (1024 * 1024), 2)


class Curso(models.Model):
    NIVELES = [
        ('PRIMARIA', 'Primaria'),
        ('SECUNDARIA', 'Secundaria'),
        ('BACHILLERATO', 'Bachillerato'),
        ('UNIVERSITARIO', 'Universitario'),
        ('POSGRADO', 'Posgrado'),
        ('LIBRE', 'Libre'),
    ]
    
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('PUBLICADO', 'Publicado'),
        ('ARCHIVADO', 'Archivado'),
    ]
    
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100, db_index=True)
    nivel = models.CharField(max_length=20, choices=NIVELES, default='LIBRE')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='BORRADOR')
    duracion_horas = models.IntegerField(default=10)
    recursos = models.ManyToManyField(RecursoEducativo, related_name='cursos', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen_url = models.URLField(blank=True, null=True)
    palabras_clave = models.CharField(max_length=500, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    class Meta:
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['categoria']),
            models.Index(fields=['nivel']),
            models.Index(fields=['estado']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.titulo} - {self.nivel}"
    
    @property
    def total_recursos(self):
        return self.recursos.count()
    
    @property
    def tamanio_total_mb(self):
        total_bytes = self.recursos.aggregate(models.Sum('tamanio_bytes'))['tamanio_bytes__sum'] or 0
        return round(total_bytes / (1024 * 1024), 2)
