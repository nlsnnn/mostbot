from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


from .serializers import BotSerializer, MessageSerializer, TaskSerializer
from .models import Bot as BotModel, Message
from .creator import Bot


class BotViewSet(ModelViewSet):
    queryset = BotModel.objects.all()
    serializer_class = BotSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bot = Bot(request.data['bot_token'])
        res = bot.send_task(request.data)

        return Response(status=HTTP_200_OK if res else HTTP_500_INTERNAL_SERVER_ERROR)