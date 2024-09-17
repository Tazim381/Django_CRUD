from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=100,null=True)
    department = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name