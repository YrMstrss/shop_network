from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from network.models import Link
from network.permissions import IsActive
from network.serializers import LinkSerializer, FactoryCreateSerializer, LinkUpdateSerializer, LinkCreateSerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания завода
    """
    serializer_class = FactoryCreateSerializer
    permission_classes = [IsActive]

    def perform_create(self, serializer):
        """
        Метод устанавливающий уровень завода в иерархии = 0
        :param serializer: Сериалайзер для создания завода
        :return: None
        """
        link = serializer.save()
        link.level = 0
        link.save()


class LinkCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания звена сети
    """
    serializer_class = LinkCreateSerializer
    permission_classes = [IsActive]

    def perform_create(self, serializer):
        """
        Метод устанавливающий уровень звена в иерархии сети
        :param serializer: Сериалайзер для создания звена сети
        :return: None
        """
        link = serializer.save()
        if link.link_type == 'Factory':
            link.level = 0
            link.save()
        else:
            if link.provider.link_type == 'Factory':
                link.level = 1
                link.save()
            else:
                link.level = 2
                link.save()


class LinkListAPIView(generics.ListAPIView):
    """
    Контроллер для просмотра списка всех звеньев сети с возможностью фильтрации по стране
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contact__country',)


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра отдельного звена сети
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActive]


class LinkUpdateAPIVIew(generics.UpdateAPIView):
    """
    Контроллер для обновления данных о звене сети
    """
    serializer_class = LinkUpdateSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActive]


class LinkDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления звена сети
    """
    queryset = Link.objects.all()
    permission_classes = [IsActive]
