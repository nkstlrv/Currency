# Generated by Django 4.2.3 on 2023-07-13 15:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0009_rename_contacts_contactus_rename_rates_rate_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactus",
            options={"verbose_name": "ContactUs", "verbose_name_plural": "ContactUs"},
        ),
    ]
