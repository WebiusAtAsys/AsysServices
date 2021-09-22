# Generated by Django 3.2.7 on 2021-09-22 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0007_alter_report_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='image1',
            field=models.ImageField(default='report.png', upload_to='report_pics'),
        ),
        migrations.AlterField(
            model_name='report',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfs'),
        ),
    ]
