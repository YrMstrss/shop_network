from django.contrib import admin
from django.utils.safestring import mark_safe

from network.models import Contact, Link
from django.utils.translation import gettext_lazy as _


class CityListFilter(admin.SimpleListFilter):

    """
    Кастомный фильтр по городу
    """

    title = _("Город")

    parameter_name = "city"

    def lookups(self, request, model_admin):

        """
        Метод для получения списка всех городов, в которых располагаются звенья сети
        :param request:
        :param model_admin:
        :return: Список городов
        """

        sidebar = []

        for contact in Contact.objects.all():
            if (contact.city, contact.city) not in sidebar:
                sidebar.append((contact.city, contact.city))

        return sidebar

    def queryset(self, request, queryset):

        """
        Метод возвращающий отфильтрованный список звеньев сети
        :param request:
        :param queryset:
        :return:
        """

        if not self.value():
            return queryset

        filtered_contacts = Contact.objects.filter(city=self.value())
        links_ids = [contact.link.id for contact in filtered_contacts]

        return queryset.filter(id__in=links_ids)


@admin.action(description='Обнулить задолженность')
def cancel_debt(modeladmin, request, queryset):
    """
    Кастомное действие для админ панели, позволяющее обнулить задолженность выбранных звеньев перед поставщиком
    """
    queryset.update(debt=0.0)


@admin.display(description='Город')
def link_city(obj):
    """
    Дополнительное поле для вывода города, в котором расположено звено сети
    :param obj: Объект Link - звено сети.
    :return: Строка с названием города, в котором расположено звено сети
    """
    contact = Contact.objects.get(link=obj.id)
    return f'{contact.city}'


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """
    Регистрация модели звена сети на админ панели
    """
    list_display = ('link_type', 'name', 'provider_link', 'debt', 'level', link_city)
    list_filter = ('link_type', 'level', CityListFilter)
    actions = [cancel_debt]

    def provider_link(self, obj):
        """
        Метод для создания поля с активной ссылкой на поставщика
        :param obj: Объект Link - звено сети
        :return: Ссылка на поставщика
        """
        if obj.provider:
            return mark_safe(f'<a href="http://127.0.0.1:8000/link/{obj.provider.id}">{obj.provider}</a>')
        else:
            return 'нет поставщика'

    provider_link.short_description = 'Поставщик'
