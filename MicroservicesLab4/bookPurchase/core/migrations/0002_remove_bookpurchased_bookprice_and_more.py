# Generated by Django 4.1.4 on 2022-12-17 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookpurchased",
            name="BookPrice",
        ),
        migrations.RemoveField(
            model_name="bookpurchased",
            name="Type",
        ),
        migrations.RemoveField(
            model_name="bookpurchased",
            name="authorName",
        ),
    ]
