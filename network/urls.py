from django.urls import path

from network.apps import NetworkConfig
from network.views import LinkCreateAPIView, LinkListAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('create/', LinkCreateAPIView.as_view(), name='create-link'),
    path('list/', LinkListAPIView.as_view(), name='list-link')
]
