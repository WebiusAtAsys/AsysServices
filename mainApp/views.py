from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from django.contrib import messages
#needed for class based view
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.
class ReportCreateView(LoginRequiredMixin, View):
    form_class = ReportForm
    initial = {}
    template_name = 'mainApp/index.html' #by default django will look in <app>/<model>_<viewtype>.html
    fields = ['title', 'description', 'laserSource', 'image']
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
        if repForm.is_valid():
            repForm.save()
            #set the user has reports field to true and save it
            self.request.user.has_reports = True
            self.request.user.save()
            print("Report saved!!")
            messages.success(request, f'Your report has been created')
            #generate the pdf here
            # first_name = request.user.first_name
            # last_name = request.user.last_name
            # title = form.cleaned_data.get('title')
        else:
            print("Fail")
            messages.error(request, f'Report could not be created. Please check your entries')
            context = {"form" : repForm}
            return render(request, self.template_name, context)
        context = {"form": repForm}
        return redirect("reports")


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
    fields = '__all__'

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

# def preview(request):
#     return render(request, "mainApp/preview.html")
