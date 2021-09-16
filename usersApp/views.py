from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    #form submitted (as post request)
    if request.method == 'POST':
        #pass the data from the request on to the UserCreationForm
        uForm = RegisterForm(request.POST)
        #django backend check
        if uForm.is_valid():
            uForm.save()
            username = uForm.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        uForm = RegisterForm()
    return render(request, "usersApp/register.html", {"form": uForm})


@login_required
def profile(request):
    if request.method == 'POST':
        upUserForm = UserUpdateForm(request.POST, instance=request.user)
        upProfileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if upUserForm.is_valid() and upProfileForm.is_valid():
            upUserForm.save()
            upProfileForm.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        upUserForm = UserUpdateForm(instance=request.user)
        upProfileForm = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'upUserForm' : upUserForm,
        'upProfileForm' : upProfileForm,
    }
    return render(request, 'usersApp/profile.html', context)