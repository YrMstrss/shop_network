from django.contrib import admin
from django.utils.safestring import mark_safe

from network.models import Contact, Link
from django.utils.translation import gettext_lazy as _


class CityListFilter(admin.SimpleListFilter):

    title = _("Город")

    parameter_name = "city"

    def lookups(self, request, model_admin):

        sidebar = []

        for contact in Contact.objects.all():
            if (contact.city, contact.city) not in sidebar:
                sidebar.append((contact.city, contact.city))

        return sidebar

    def queryset(self, request, queryset):

        if not self.value():
            return queryset

        filtered_contacts = Contact.objects.filter(city=self.value())
        links_ids = [contact.link.id for contact in filtered_contacts]

        return queryset.filter(id__in=links_ids)


@admin.action(description='Обнулить задолженность')
def cancel_debt(modeladmin, request, queryset):
    queryset.update(debt=0.0)


@admin.display(description='Город')
def link_city(obj):
    contact = Contact.objects.get(link=obj.id)
    return f'{contact.city}'


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('link_type', 'name', 'provider_link', 'debt', 'level', link_city)
    list_filter = ('link_type', 'level', CityListFilter)
    actions = [cancel_debt]

    def provider_link(self, obj):
        if obj.provider:
            return mark_safe(f'<a href="http://127.0.0.1:8000/link/{obj.provider.id}">{obj.provider}</a>')
        else:
            return 'нет поставщика'

    provider_link.short_description = 'Поставщик'
