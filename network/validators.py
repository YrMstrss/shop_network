from rest_framework.exceptions import ValidationError


class LinkFactoryProviderValidator:

    """Валидатор для проверки отсутствия у завода поставщика"""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        tmp_value_1 = dict(value).get(self.field_1)
        tmp_value_2 = dict(value).get(self.field_2)

        if tmp_value_1 == 'Factory' and tmp_value_2:
            raise ValidationError('У завода не должно быть поставщика')


class LinkFactoryDebtValidator:

    """Валидатор для проверки отсутствия у завода долга"""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        tmp_value_1 = dict(value).get(self.field_1)
        tmp_value_2 = dict(value).get(self.field_2)

        if tmp_value_1 == 'Factory' and tmp_value_2:
            raise ValidationError('У завода не может быть долга перед поставщиком')
