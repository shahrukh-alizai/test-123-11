# Generated by Django 2.2.14 on 2020-07-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_auto_20200729_1120"),
    ]

    operations = [
        migrations.RemoveField(model_name="homepage", name="tests",),
    ]
