# Generated by Django 3.2.7 on 2021-09-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filltexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(max_length=1000)),
                ('text2', models.TextField(max_length=1000)),
                ('text3', models.TextField(max_length=1000)),
                ('text4', models.TextField(max_length=1000)),
                ('text5', models.TextField(max_length=1000)),
            ],
        ),
    ]