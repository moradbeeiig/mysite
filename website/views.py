from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_views(request):
    return render(request,'website\index.html')

def about_views(request):
    return render(request,'website\About.html')

def contact_views(request):
    return render(request,'website\contact.html')
    # return HttpResponse ("<h1>Contacts page</h1>")

