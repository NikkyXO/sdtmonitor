# Generated by Django 4.1.5 on 2023-01-09 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wsite", "0002_emails"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Emails",
            new_name="WebsiteEmail",
        ),
        migrations.RenameModel(
            old_name="Log",
            new_name="WebsiteLog",
        ),
    ]
