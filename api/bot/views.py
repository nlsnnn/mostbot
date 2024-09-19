from rest_framework.viewsets import ModelViewSet

from .serializers import BotSerializer
from .models import Bot as BotModel


class BotViewSet(ModelViewSet):
    queryset = BotModel.objects.all()
    serializer_class = BotSerializer
