from rest_framework import serializers

from network.models import Link, Contact
from network.validators import LinkFactoryProviderValidator, LinkFactoryDebtValidator


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class LinkCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Link
        exclude = ('level',)
        validators = [
            LinkFactoryProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def create(self, validated_data):
        contact = validated_data.pop('contact')

        link = Link.objects.create(**validated_data)
        Contact.objects.create(**contact, link=link)

        return link


class LinkSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Link
        fields = '__all__'


class LinkUpdateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('debt', 'level', )
        validators = [
            LinkFactoryProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def update(self, instance, validated_data):
        if 'contact' in validated_data.keys():
            contact = validated_data.pop('contact')

            super().update(instance, validated_data)
            super().update(instance.contact, contact)
        else:
            super().update(instance, validated_data)

        return instance
