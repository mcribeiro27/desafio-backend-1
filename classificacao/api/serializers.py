from rest_framework.serializers import ModelSerializer
from classificacao.models import Classificacao

# Arquivo para serializar nossos dados
class ClassificacaoSerializer(ModelSerializer):
    class Meta:
        model = Classificacao
        fields = ('id', 'classificacao',)