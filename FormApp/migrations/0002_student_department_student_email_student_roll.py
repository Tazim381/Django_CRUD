# Generated by Django 4.2.16 on 2024-09-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
