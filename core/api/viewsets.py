from rest_framework.viewsets import ModelViewSet
from core.models import Viagem
from .serializers import ViagemSerializer

class ViagemViewSet(ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer
