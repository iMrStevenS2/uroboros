# Generated by Django 4.1 on 2024-05-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
