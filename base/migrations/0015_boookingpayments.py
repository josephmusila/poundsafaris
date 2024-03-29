# Generated by Django 5.0 on 2024-01-16 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0014_rename_item_cart_trips_cart_total"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoookingPayments",
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
                    "amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("reference", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "payment_method",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "confirmation_code",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "payment_status_description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "payment_account",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "merchant_reference",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("currency", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "order_tracking_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("create_date", models.DateTimeField(blank=True, null=True)),
                ("message", models.CharField(blank=True, max_length=100, null=True)),
                ("status_code", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "payment_status_code",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("status", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "booking",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="base.booking",
                    ),
                ),
            ],
        ),
    ]
