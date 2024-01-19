from django.contrib.auth.models import AbstractUser
from django.db import models

from employee.managers import UserManager


class Employee(AbstractUser):

    is_active = models.BooleanField(default=False, verbose_name='активен')

    email = models.EmailField(unique=True, verbose_name='почта')
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
