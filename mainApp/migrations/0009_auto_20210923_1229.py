# Generated by Django 3.2.7 on 2021-09-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20210922_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='beamExpander',
            field=models.CharField(blank=True, choices=[('8x motorized', '8x motorized')], default='8x motorized', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='beamSource',
            field=models.CharField(blank=True, choices=[('Innolas Blizz', 'Innolas Blizz'), ('Eolite', 'Eolite'), ('CO2', 'CO2')], default='CO2', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='customerEmail',
            field=models.CharField(blank=True, default='customer.company@example.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='customerId',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='customerName',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='customerPlz',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='customerStreet',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='customerTel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='image1',
            field=models.ImageField(blank=True, default='report.png', upload_to='report_pics'),
        ),
        migrations.AlterField(
            model_name='report',
            name='lens',
            field=models.CharField(blank=True, choices=[('255 mm f-theta', '255 mm f-theta')], default='255 mm f-theta', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='machine',
            field=models.CharField(blank=True, choices=[('Divisio 9000', 'Divisio 9000'), ('Insignum 2000', 'Insignum 2000')], default='Divisio 9000', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='material',
            field=models.CharField(blank=True, choices=[('FR4', 'FR4'), ('Kunststoff', 'Kunststoff'), ('V2A', 'V2A'), ('Aluminium', 'Aluminium'), ('Keramik', 'Keramik')], default='FR4', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='maxPower',
            field=models.CharField(blank=True, default='40 W', max_length=10),
        ),
        migrations.AlterField(
            model_name='report',
            name='microscope',
            field=models.CharField(blank=True, choices=[('Keyence VHX-7100 Digital Microscope', 'Keyence VHX-7100 Digital Microscope')], default='Keyence VHX-7100 Digital Microscope', max_length=40),
        ),
        migrations.AlterField(
            model_name='report',
            name='numberParts',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='report',
            name='sampleHeigth',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='report',
            name='sampleThickness',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='report',
            name='sampleWidth',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='report',
            name='scanField',
            field=models.CharField(blank=True, choices=[('100 x 100 mm^2', '100 x 100 mm^2'), ('150 x 150 mm^2', '150 x 150 mm^2'), ('180 x 180 mm^2', '180 x 180 mm^2')], default='100 x 100 mm^2', max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='spotSize',
            field=models.CharField(blank=True, default='50 um 1/e^2', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='task',
            field=models.CharField(blank=True, choices=[('Laser depaneling', 'Laser depaneling'), ('Laser marking', 'Laser marking'), ('Laser engraving', 'Laser engraving')], default='Laser depaneling', max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='wavelength',
            field=models.CharField(blank=True, choices=[('1064 nm', '1064 nm'), ('532 nm', '532 nm'), ('265 nm', '265 nm')], default='532 nm', max_length=10),
        ),
    ]
