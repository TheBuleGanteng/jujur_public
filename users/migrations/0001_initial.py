# Generated by Django 5.0.3 on 2024-03-29 03:47

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
            name="UserProfile",
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
                (
                    "cash",
                    models.DecimalField(
                        decimal_places=2, default=10000.0, max_digits=10
                    ),
                ),
                (
                    "cash_initial",
                    models.DecimalField(
                        decimal_places=2, default=10000.0, max_digits=10
                    ),
                ),
                ("accounting_method", models.CharField(default="FIFO", max_length=64)),
                ("tax_loss_offsets", models.CharField(default="On", max_length=64)),
                (
                    "tax_rate_STCG",
                    models.DecimalField(decimal_places=2, default=15.0, max_digits=5),
                ),
                (
                    "tax_rate_LTCG",
                    models.DecimalField(decimal_places=2, default=30.0, max_digits=5),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
