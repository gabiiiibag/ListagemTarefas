# Generated by Django 5.0.1 on 2024-01-25 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toDo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="entrega",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 25, 14, 43, 39, 436861, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="todo",
            name="finalizacao",
            field=models.DateTimeField(null=True),
        ),
    ]
