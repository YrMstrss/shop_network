from rest_framework import serializers

from network.models import Link, Contact, Product
from network.validators import LinkFactoryProviderValidator, LinkFactoryDebtValidator, FactoryValidator


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FactoryCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Link
        exclude = ('level',)
        validators = [
            FactoryValidator(field='link_type'),
            LinkFactoryProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def create(self, validated_data):
        contact = validated_data.pop('contact')
        products = validated_data.pop('products')

        link = Link.objects.create(**validated_data)
        Contact.objects.create(**contact, link=link)

        for product in products:
            prod = Product.objects.create(**product)
            link.products.add(prod)

        return link


class LinkCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Link
        exclude = ('level',)
        validators = [
            LinkFactoryProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def create(self, validated_data):
        contact = validated_data.pop('contact')
        products = validated_data.pop('products')

        link = Link.objects.create(**validated_data)
        Contact.objects.create(**contact, link=link)

        for product in products:
            prod = Product.objects.get(**product)
            link.products.add(prod)

        return link


class LinkSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Link
        fields = '__all__'


class LinkUpdateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('debt', 'level',)
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
