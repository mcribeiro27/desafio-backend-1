from rest_framework.viewsets import ModelViewSet
from classificacao.models import Classificacao
from .serializers import ClassificacaoSerializer


class ClassificacaoViewSet(ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer