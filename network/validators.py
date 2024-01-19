from rest_framework.exceptions import ValidationError


class FactoryValidator:
    """
    Валидатор для проверки является ли звено заводом
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if not tmp_value == 'Factory':
            raise ValidationError('Создаваемое звено сети должно быть заводом')


class LinkProviderValidator:
    """
    Валидатор для проверки отсутствия у завода поставщика
    """

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        tmp_value_1 = dict(value).get(self.field_1)
        tmp_value_2 = dict(value).get(self.field_2)

        if tmp_value_1 == 'Factory' and tmp_value_2:
            raise ValidationError('У завода не должно быть поставщика')

        if tmp_value_1 == 'Company' or tmp_value_1 == 'Retail':
            if not tmp_value_2:
                raise ValidationError('ИП или розничная сеть должны иметь поставщика')


class LinkFactoryDebtValidator:
    """
    Валидатор для проверки отсутствия у завода долга
    """

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        tmp_value_1 = dict(value).get(self.field_1)
        tmp_value_2 = dict(value).get(self.field_2)

        if tmp_value_1 == 'Factory' and tmp_value_2:
            raise ValidationError('У завода не может быть долга перед поставщиком')
