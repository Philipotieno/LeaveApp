# Generated by Django 3.2 on 2022-02-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Leave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "leave_type",
                    models.CharField(
                        choices=[
                            ("Normal leave", "Normal leave"),
                            ("Sick leave", "Sick leave"),
                        ],
                        default="Normal leave",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "db_table": "leave",
            },
        ),
    ]
