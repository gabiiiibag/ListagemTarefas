# Generated by Django 5.0.1 on 2024-02-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toDo", "0003_alter_todo_entrega_alter_todo_titulo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="finalizacao",
            field=models.DateField(null=True),
        ),
    ]