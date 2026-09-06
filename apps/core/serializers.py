from rest_framework import serializers
from .models import RecursoEducativo, Curso


class RecursoEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoEducativo
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    # Para lectura: muestra los recursos detallados
    recursos_detalle = RecursoEducativoSerializer(source='recursos', many=True, read_only=True)
    
    # Para escritura: acepta una lista de IDs de recursos
    recursos = serializers.PrimaryKeyRelatedField(
        queryset=RecursoEducativo.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'descripcion',
            'categoria',
            'nivel',
            'estado',
            'duracion_horas',
            'recursos',
            'recursos_detalle',
            'fecha_creacion',
            'fecha_actualizacion',
        ]
