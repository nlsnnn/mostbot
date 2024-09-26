from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BotViewSet, MessageViewSet, TaskView

router = DefaultRouter()
router.register("bots", BotViewSet)
router.register("message", MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('task/', TaskView.as_view())
]