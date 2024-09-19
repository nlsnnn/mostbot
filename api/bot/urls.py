from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BotViewSet

router = DefaultRouter()
router.register("bots", BotViewSet)

urlpatterns = [
    path('', include(router.urls))
]