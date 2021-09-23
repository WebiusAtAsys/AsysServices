from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from django.contrib import messages
#needed for class based view
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
#needed for file handling
from django.http import FileResponse
from django.core.files.base import ContentFile
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
#from . import pdf_creater

# Create your views here.
class ReportCreateView(LoginRequiredMixin, View):
    form_class = ReportForm
    initial = {}
    template_name = 'mainApp/index.html' #by default django will look in <app>/<model>_<viewtype>.html
    #fields = ['date', 'title', 'description', 'beamSource', 'image1']
    def get(self, request, *args, **kwargs):
        #GET method
        repForm = self.form_class(initial=self.initial)
        context = {"form" : repForm}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        #POST method
        repForm = self.form_class(request.POST, request.FILES)
        #note in form which user created it
        repForm.instance.author = self.request.user
        #check if submitted form is valid
        if repForm.is_valid():
            #create report instance but dont send it to database yet, cause
            #there is more to be added
            report = repForm.save(commit=False)

            #generate pdf here
            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
            textobj = c.beginText()
            textobj.setTextOrigin(inch, inch)
            textobj.setFont("Helvetica", 14)
            #queryset = Report.objects.filter(author=self.request.user)
            lines = [
                repForm.instance.title,
                repForm.instance.description,
            ]
            for line in lines:
                textobj.textLine(line)

            c.drawText(textobj)
            c.showPage()
            c.save()
            buf.seek(0)
            #create a new report instance (instance = model-object)
            #with the author beeing the user submitting the form
            report.pdf.save("report.pdf", buf)
            report.save()
            #get the primary key of the just saved report for redirection
            pk = report.id
            #set the user has reports field to true and save it
            self.request.user.has_reports = True
            self.request.user.save()
            messages.success(request, f'Your report has been created')
            print("Report saved!")
        else:
            print("Fail")
            messages.error(request, f'Report could not be created. Please check your entries')
            context = {"form" : repForm}
            return render(request, self.template_name, context)
        url = 'report/' + str(pk) + '/download'
        return redirect(url)
        #return redirect('reports') uncomment this line to change redirection to report list

class ReportListView(ListView):
    #tell the class what objects to query, cause needed for the list:
    model = Report
    template_name = "mainApp/report_list.html"
    context_object_name = "reports"
    ordering = ["-date"]

class ReportDetailView(DetailView):
    #tell the class what objects to query, cause needed for the list:
    model = Report
    template_name = "mainApp/report_detail.html"
    fields = '__all__'

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #tell the class what objects to query, cause needed for the list:
    model = Report
    template_name = "mainApp/report_update.html"
    fields = ['date', 'title', 'description', 'customerId', 'customerName', 'customerStreet', 'customerPlz', 'customerTel', 'customerEmail',
    'task', 'material', 'numberParts', 'machine', 'microscope', 'beamSource', 'wavelength', 'maxPower', 'beamExpander', 'lens', 'spotSize',
    'scanField', 'sampleWidth', 'sampleHeigth', 'sampleThickness', 'image1']
    
    #if receiving a post request this means the user wants to update a report
    def post(self, request, pk, *args, **kwargs):
        #POST method
        repForm = ReportForm(request.POST, request.FILES)
        #check if submitted form is valid
        if repForm.is_valid():
            #get the instance which shall be updated:
            report = Report.objects.get(pk=pk) #self.get_object().id
            #update the instance with the new values
            for key, value in repForm.cleaned_data.items():
                setattr(report, key, value)

            #generate the new pdf
            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
            textobj = c.beginText()
            textobj.setTextOrigin(inch, inch)
            textobj.setFont("Helvetica", 14)
            #queryset = Report.objects.filter(author=self.request.user)
            lines = [
                repForm.instance.title,
                repForm.instance.description,
            ]
            for line in lines:
                textobj.textLine(line)

            c.drawText(textobj)
            c.showPage()
            c.save()
            buf.seek(0)
            report.pdf.save("report.pdf", buf)
            #save the updated instance
            report.save()
            messages.success(request, f'Your report has been updated')
            print("Report saved!")
        else:
            print("Fail")
            messages.error(request, f'Report could not be updated. Please check your entries')
            context = {"form" : repForm}
            return render(request, self.template_name, context)
        #url = 'report/' + str(pk) + "/"
        return redirect("reports")

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.author:
            return True
        return False

class ReportDeleteView(LoginRequiredMixin, DeleteView):
    #tell the class what objects to query, cause needed for the list:
    model = Report
    template_name = "mainApp/report_confirm_delete.html"
    success_url = '/'

def download(request, pk):
    report = Report.objects.get(pk=pk)
    request = FileResponse(open(report.pdf.path, 'rb'))
    return request