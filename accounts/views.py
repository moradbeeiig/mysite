from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

@csrf_exempt
def login_views(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect ('/')
        form=AuthenticationForm()
        context={'form':form}
        return render (request,'accounts/login.html',context)
    else:
        return redirect ('/')
    
@login_required
def logout_views(request):
    logout(request)       
    return redirect('/')

@csrf_exempt
def signup_views(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form=UserCreationForm()
        contex={"form":form}
        return render (request,'accounts/signup.html',contex)
    else:
        return redirect('/')
