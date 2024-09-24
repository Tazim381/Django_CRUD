from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def validate_roll(value):
    if not value.isdigit():
        raise ValidationError('Roll must contain only digits')


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20, null=True, validators=[validate_roll])
    email = models.EmailField(max_length=100, null=True)
    department = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

