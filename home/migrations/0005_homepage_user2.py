# Generated by Django 2.2.14 on 2020-07-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_rwat"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="user2",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
