# Generated by Django 5.0.7 on 2024-07-12 03:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(null=True)),
                ("name", models.CharField(max_length=64)),
                ("size", models.CharField(max_length=32)),
                ("current_price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("min_price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_by_id", models.BigIntegerField(null=True)),
                ("updated_by_id", models.BigIntegerField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="relation users",
                    ),
                ),
            ],
        ),
    ]
