# Generated by Django 3.2.5 on 2021-09-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_reports',
            field=models.BooleanField(default=False),
        ),
    ]
