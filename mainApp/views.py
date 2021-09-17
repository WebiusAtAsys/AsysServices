from django.shortcuts import render, redirect
from .forms import ReportForm
from django.contrib import messages
#needed for class based view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

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
            print("Report saved!!")
            messages.success(request, f'Your report was created')
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
        return redirect("preview")


def preview(request):
    return render(request, "mainApp/preview.html")
