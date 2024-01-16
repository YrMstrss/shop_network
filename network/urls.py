from django.urls import path

from network.apps import NetworkConfig
from network.views import FactoryCreateAPIView, LinkListAPIView, LinkRetrieveAPIView, LinkUpdateAPIVIew, \
    LinkDestroyAPIView, LinkCreateAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('factory/create/', FactoryCreateAPIView.as_view(), name='create-factory'),
    path('create/', LinkCreateAPIView.as_view(), name='create-link'),
    path('list/', LinkListAPIView.as_view(), name='list-link'),
    path('<int:pk>/', LinkRetrieveAPIView.as_view(), name='retrieve-link'),
    path('edit/<int:pk>/', LinkUpdateAPIVIew.as_view(), name='update-link'),
    path('delete/<int:pk>/', LinkDestroyAPIView.as_view(), name='destroy-link'),
]
