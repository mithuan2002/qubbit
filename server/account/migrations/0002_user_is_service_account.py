# Generated by Django 4.2.16 on 2024-12-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_service_account',
            field=models.BooleanField(default=False),
        ),
    ]
