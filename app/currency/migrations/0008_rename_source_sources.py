# Generated by Django 4.2.3 on 2023-07-04 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_alter_rates_source'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Source',
            new_name='Sources',
        ),
    ]
