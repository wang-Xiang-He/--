# Generated by Django 2.1 on 2020-02-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20200216_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
