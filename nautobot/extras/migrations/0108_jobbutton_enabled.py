# Generated by Django 3.2.25 on 2024-06-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0107_laxurlfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobbutton",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]
