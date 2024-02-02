# Generated by Django 5.0.1 on 2024-01-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toDo", "0002_todo_entrega_todo_finalizacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="entrega",
            field=models.DateField(verbose_name="Entrega"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="titulo",
            field=models.CharField(max_length=100, verbose_name="Título"),
        ),
    ]