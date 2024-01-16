from django.core.management import BaseCommand

from employee.models import Employee


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = Employee.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            last_name='Shops',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        admin.set_password('password')
        admin.save()
