# Generated by Django 4.1 on 2024-05-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_tareas', '0003_avance_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
