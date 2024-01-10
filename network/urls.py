from django.urls import path

from network.apps import NetworkConfig
from network.views import LinkCreateAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('create/', LinkCreateAPIView.as_view(), name='create-link'),
]
