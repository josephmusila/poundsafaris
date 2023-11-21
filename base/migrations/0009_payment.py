# Generated by Django 3.2.23 on 2023-11-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_tourcategory_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]