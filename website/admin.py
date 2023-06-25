from django.contrib import admin
from website.models import Contact

class contactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display=["name","Email","subject"]
    list_filter=["Email"]
    search_fields=['name','message']

admin.site.register(Contact,contactAdmin)
# Register your models here.
