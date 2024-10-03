from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "password", "re_password")


    def create(self, validated_data):
        print(f'LOOOOOOOOL')
        email = validated_data['email']

        username = email.split('@')[0]

        validated_data['username'] = username

        return super().create(validated_data)