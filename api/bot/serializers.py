from rest_framework.serializers import ModelSerializer

from .models import Bot as BotModel
from .creator import Bot


class BotSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BotModel

    def create(self, validated_data):
        bot = Bot(validated_data['token'])

        bot.start_thread(validated_data['template'])
        return super().create(validated_data)