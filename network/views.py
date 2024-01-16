from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from network.models import Link
from network.serializers import LinkSerializer, FactoryCreateSerializer, LinkUpdateSerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    serializer_class = FactoryCreateSerializer

    def perform_create(self, serializer):
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
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contact__country', )


class LinkUpdateAPIVIew(generics.UpdateAPIView):
    serializer_class = LinkUpdateSerializer
    queryset = Link.objects.all()


class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
