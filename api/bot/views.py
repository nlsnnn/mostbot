from rest_framework.viewsets import ModelViewSet

from .serializers import BotSerializer, MessageSerializer
from .models import Bot as BotModel, Message


class BotViewSet(ModelViewSet):
    queryset = BotModel.objects.all()
    serializer_class = BotSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer