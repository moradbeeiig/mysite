from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsLetterForm
from django.contrib import messages


def index_views(request):
    return render(request,'website\index.html')

def about_views(request):
    return render(request,'website\About.html')

def contact_views(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticked submited successfully')
        else:
            messages.add_message(request,messages.ERROR,"your ticket did't Submited")    
    form=ContactForm()
    return render(request,'website\contact.html',{'form':form})


def newsletter_views(request):
    if request.method=='POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')






def test_views(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['Email']
            # subject=form.cleaned_data['subject']
            # message=form.cleaned_data['massage']
            # print(name,email,subject,message)
            return HttpResponse("done")
        else:
            return HttpResponse("wrong input informations")
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # subject=request.POST.get('subject')
        # message=request.POST.get('massage')
        # c=Contact()
        # c.name=name
        # c.Email=email
        # c.subject=subject
        # c.message=message
        # c.save()
    form=ContactForm()
    return render(request,'test.html',{'form':form})




