from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from travel.models import TravelModel
from announcement.models import AnnouncementModel
# Create your views here.

def signup(request):
    if request.method=="POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            auth_login(request, user)

            return redirect('home:index')
    else:
        form=SignUpForm()
    return render(request,'account/signup.html',{'form':form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home:index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})



def logout(request):
    auth_logout(request)
    return redirect('home:index')


def profile(request):
    travels=TravelModel.objects.filter(author=request.user)
    posts= AnnouncementModel.objects.filter(author=request.user)
    return render(request,'account/profile.html',{'travels':travels,'posts':posts})
