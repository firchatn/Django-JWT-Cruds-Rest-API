# Generated by Django 4.1.2 on 2023-06-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backjwtcruds", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="phone",
            field=models.CharField(default=22222222, max_length=20),
            preserve_default=False,
        ),
    ]
