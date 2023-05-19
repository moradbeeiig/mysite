from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_views),
    path('About',about_views),
    path('Contacts',contact_views)
]