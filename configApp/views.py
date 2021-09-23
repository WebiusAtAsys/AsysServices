#from django.shortcuts import render
from .forms import FilltextsForm
from .models import Filltexts
from django.views.generic import UpdateView, CreateView
#from django.views import View
from django.shortcuts import render, redirect

class FilltextsCreateView(CreateView):
    model = Filltexts
    form_class = FilltextsForm
    template_name = "configApp/adjust.html"
    context_object_name = "textblocks"
    #fields = '__all__'

# Create your views here.
class FilltextsUpdateView(UpdateView):
    model = Filltexts
    form_class = FilltextsForm
    template_name = "configApp/adjust.html"
    context_object_name = "textblocks"
    #fields = '__all__'
    #ordering = ["-date"]

    # def post(self, request, *args, **kwargs):
    #     #POST method
    #     textForm = self.form_class(request.POST)
    #     #check if submitted form is valid
    #     if textForm.is_valid():
    #         textForm.save()
        
    #     context = {"form" : textForm}
    #     return render(request, self.template_name, context)
    
    # def get(self, request, *args, **kwargs):
    #     textForm = self.form_class(initial=self.initial)
    #     context = {"form" : textForm}
    #     return render(request, self.template_name, context)



# def adjust(request):
#     if request.method == "POST":
#         repForm = self.form_class(initial=self.initial)
#         context = {"form" : repForm}
#         return render(request, self.template_name, context)