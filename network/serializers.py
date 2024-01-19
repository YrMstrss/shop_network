from rest_framework import serializers

from network.models import Link, Contact, Product
from network.validators import LinkProviderValidator, LinkFactoryDebtValidator, FactoryValidator


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели контакта
    """
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели продукта
    """
    class Meta:
        model = Product
        fields = '__all__'


class FactoryCreateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для создания завода
    """
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Link
        exclude = ('level',)
        validators = [
            FactoryValidator(field='link_type'),
            LinkProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def create(self, validated_data):
        """
        Метод, позволяющий при создании завода создавать так же связанные с ним объекты контактов и производимых
        продуктов
        :param validated_data: Отвалидированные данные
        :return: Созданный объект Link
        """
        contact = validated_data.pop('contact')
        products = validated_data.pop('products')

        link = Link.objects.create(**validated_data)
        Contact.objects.create(**contact, link=link)

        for product in products:
            prod = Product.objects.create(**product)
            link.products.add(prod)

        return link


class LinkCreateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для создания звеньев сети, не являющихся заводом
    """
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Link
        exclude = ('level',)
        validators = [
            LinkProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def create(self, validated_data):
        """
        Метод, позволяющий при создании звена сети создавать так же связанные с ним объекты контактов и добавлять
        продукты
        :param validated_data: Отвалидированные данные
        :return: Созданный объект Link
        """
        contact = validated_data.pop('contact')
        products = validated_data.pop('products')

        link = Link.objects.create(**validated_data)
        Contact.objects.create(**contact, link=link)

        for product in products:
            prod = Product.objects.get(**product)
            link.products.add(prod)

        return link


class LinkSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для вывода и удаления объекты Link
    """
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Link
        fields = '__all__'


class LinkUpdateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для редактирования объектов Link
    """
    contact = ContactSerializer()
    products = ProductSerializer()

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('debt', 'level',)
        validators = [
            LinkProviderValidator(field_1='link_type', field_2='provider'),
            LinkFactoryDebtValidator(field_1='link_type', field_2='debt'),
        ]

    def update(self, instance, validated_data):
        """
        Метод для обновления данных о существующем звене сети Link и контактной информации
        :param instance: Изменяемый объект Link
        :param validated_data: Отвалидированные данные
        :return: Измененный объект Link
        """
        if 'contact' in validated_data.keys():
            contact = validated_data.pop('contact')

            super().update(instance, validated_data)
            super().update(instance.contact, contact)
        else:
            super().update(instance, validated_data)

        return instance
