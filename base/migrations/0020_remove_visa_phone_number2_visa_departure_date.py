# Generated by Django 5.0 on 2024-01-16 22:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0019_alter_visa_invitation_letter_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visa",
            name="phone_number2",
        ),
        migrations.AddField(
            model_name="visa",
            name="departure_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
