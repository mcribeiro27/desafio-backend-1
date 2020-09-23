from rest_framework.serializers import ModelSerializer
from classificacao.models import Classificacao

class ClassificacaoSerializer(ModelSerializer):
    class Meta:
        model = Classificacao
        fields = ('id', 'classificacao',)