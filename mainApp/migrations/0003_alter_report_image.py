# Generated by Django 3.2.5 on 2021-09-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_report_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(upload_to='report_pics'),
        ),
    ]