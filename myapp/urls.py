from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register_feedback', Customer_feedback, basename='feedback')
router.register('filter_topic', filter_topic, basename='filter_topic')

urlpatterns = [
    path("",include(router.urls)),
]