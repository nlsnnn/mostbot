from django.db import models
from django.contrib.auth import get_user_model


class Bot(models.Model):
    class Templates(models.TextChoices):
        SANDBOX = ("sandbox", "Песочница")
        FEEDBACK = ("feedback", "Обратная связь")


    token = models.CharField(max_length=50)
    template = models.CharField(max_length=30, choices=Templates.choices)
    name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)