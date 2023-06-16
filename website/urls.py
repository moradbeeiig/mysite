from django.urls import path
from website.views import *

app_name= 'website'

urlpatterns = [
    path('',index_views,name="index"),
    path('About',about_views,name='about'),
    path('Contacts',contact_views,name='contact')
]