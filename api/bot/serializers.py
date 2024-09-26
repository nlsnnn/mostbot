from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Bot as BotModel, Message
from .creator import Bot


class BotSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BotModel

    def create(self, validated_data):
        bot = Bot(validated_data['token'])

        name, username = bot.get_bot_info()
        validated_data['name'] = name
        validated_data['username'] = username

        bot.start_thread(validated_data['template'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data['is_active']:
            bot = Bot(instance.token)
            bot.start_thread(instance.template)

        return super().update(instance, validated_data)


class MessageSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Message

    def create(self, validated_data):
        bot = BotModel.objects.get(token=self.initial_data['bot_token'])

        validated_data['bot'] = bot

        return super().create(validated_data)


class TaskSerializer(Serializer):
    bot_token = serializers.CharField()
    type = serializers.CharField(max_length=30)
    message = serializers.CharField(required=False)
    command = serializers.CharField(max_length=20, required=False)
    new_response = serializers.CharField(required=False)