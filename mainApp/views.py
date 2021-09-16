from django.shortcuts import render, redirect
from .forms import ReportForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    #form submitted (as post request)
    if request.method == 'POST':
        #pass the data from the request on to the UserCreationForm
        repForm = ReportForm(request.POST)
        #django backend check
        if repForm.is_valid():
            repForm.save()
            #generate the pdf here
            if request.user.is_authenticated:
                first_name = request.user.first_name
                last_name = request.user.last_name

            title = repForm.cleaned_data.get('title')

            return redirect('preview')
    else:
        repForm = ReportForm()
    return render(request, "mainApp/index.html", {"form": repForm})

def preview(request):
    return render(request, "mainApp/preview.html")

    # if request.method == "POST":
    #     print("POST: ", request.POST)
    #     if request.POST.get("logout"):
    #         print("User will be logged out")
    #         return HttpResponseRedirect("/logout") #goto django built in logout
    #     elif request.POST.get("toggleGarage"):
    #         print("The garage was opened/closed")
    # return render(request, "mainApp/index.html", {})