from rest_framework.serializers import ModelSerializer
from core.models import Viagem

class ViagemSerializer(ModelSerializer):
    class Meta:
        model = Viagem
        fields = ('dt_inicio', 'dt_fim', 'classificacao', 'nota')