from rest_framework import generics

from network.serializers import LinkSerializer


class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer

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
