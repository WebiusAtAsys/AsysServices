from django.db import models
from PIL import Image
from django.urls import reverse
from PIL import Image
#from usersApp.models import User
from django.utils import timezone
#needed for file save procedure:
from django.core.files.base import File
#needed for custom user model
from django.contrib.auth import get_user_model
User = get_user_model()

#Tuple Lists for select widgets:
#the tuples are in the form ('key', 'display')
BEAM_SOURCES = [
    ('Innolas Blizz', 'Innolas Blizz'),
    ('Eolite', 'Eolite'),
    ('CO2', 'CO2')
]

WAVELENGTHS = [
    ('1064 nm', '1064 nm'),
    ('532 nm', '532 nm'),
    ('265 nm', '265 nm'),
]

BEAMEXPANDERS = [
    ('8x motorized', '8x motorized'),
]

LENSES = [
    ('255 mm f-theta', '255 mm f-theta'),
]

SCANFIELDS = [
    ('100 x 100 mm^2', '100 x 100 mm^2'),
    ('150 x 150 mm^2', '150 x 150 mm^2'),
    ('180 x 180 mm^2', '180 x 180 mm^2'),
]

MACHINE_CHOICES = [
    ('Divisio 9000', 'Divisio 9000'),
    ('Insignum 2000', 'Insignum 2000')
]

TASKS = [
    ('Laser depaneling', 'Laser depaneling'),
    ('Laser marking', 'Laser marking'),
    ('Laser engraving', 'Laser engraving')
]

MATERIALS = [
    ('FR4', 'FR4'),
    ('Kunststoff', 'Kunststoff'),
    ('V2A', 'V2A'),
    ('Aluminium', 'Aluminium'),
    ('Keramik', 'Keramik'),
]

MICROSCOPES = [
    ('Keyence VHX-7100 Digital Microscope', 'Keyence VHX-7100 Digital Microscope'),
]

# Create your models here.
class Report(models.Model):
    #all reports have an associated author/user, when the user is deleted dont delete the reports
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_DEFAULT, related_name="reports") #this will allow to query: thisUser.reports.all()
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    ############ customer fields ##################
    #using blank=True results in Views with model=Report to not require those fields in the form
    customerId = models.CharField(max_length=20, blank=True)
    customerName = models.CharField(max_length=30, blank=True)
    customerStreet = models.CharField(max_length=30, blank=True)
    customerPlz = models.CharField(max_length=30, blank=True)
    customerTel = models.CharField(max_length=20, blank=True)
    customerEmail = models.CharField(default='customer.company@example.com', max_length=50, blank=True)
    ############ task fields ##################
    task = models.CharField(max_length=30, default="Laser depaneling", choices=TASKS, blank=True)
    material = models.CharField(max_length=20, default="FR4", choices=MATERIALS, blank=True)
    numberParts = models.CharField(max_length=6, blank=True)
    ################ used tools ###############
    machine = models.CharField(max_length=20, default="Divisio 9000", choices=MACHINE_CHOICES, blank=True)
    microscope = models.CharField(max_length=40, default='Keyence VHX-7100 Digital Microscope', choices=MICROSCOPES, blank=True)
    ############ laser parameters #############
    beamSource = models.CharField(max_length=20, default="CO2", choices=BEAM_SOURCES, blank=True)
    wavelength = models.CharField(max_length=10, default='532 nm', choices=WAVELENGTHS, blank=True)
    maxPower = models.CharField(max_length=10, default='40 W', blank=True)
    beamExpander = models.CharField(max_length=20, default='8x motorized', choices=BEAMEXPANDERS, blank=True)
    lens = models.CharField(max_length=20, default='255 mm f-theta', choices=LENSES, blank=True)
    spotSize = models.CharField(max_length=20, default='50 um 1/e^2', blank=True)
    scanField = models.CharField(max_length=30, default='100 x 100 mm^2', choices=SCANFIELDS, blank=True)
    ############### sample fields #############
    sampleWidth = models.CharField(max_length=6, blank=True)
    sampleHeigth = models.CharField(max_length=6, blank=True)
    sampleThickness = models.CharField(max_length=6, blank=True)
    ################ images ###################
    image1 = models.ImageField(upload_to='report_pics', default='report.png', blank=True)
    ################ pdf field ################
    pdf = models.FileField(upload_to='pdfs', blank=True)

    #this is the function which django tries to call after the submission of a Report
    #reverse will return a path as a string so the view knows where to go
    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image1.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image1.path)