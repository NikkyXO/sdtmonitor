# Generated by Django 4.1.5 on 2023-01-12 07:29

from django.db import migrations, models
import sdtmonitor.utils.strings


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                default=sdtmonitor.utils.strings.get_slug_text,
                max_length=255,
                unique=True,
            ),
        ),
    ]
