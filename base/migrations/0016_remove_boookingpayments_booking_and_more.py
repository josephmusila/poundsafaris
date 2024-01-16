# Generated by Django 5.0 on 2024-01-16 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0015_boookingpayments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="boookingpayments",
            name="booking",
        ),
        migrations.AddField(
            model_name="boookingpayments",
            name="tour",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="base.tourcategory",
            ),
        ),
    ]
