from django.contrib import admin
from blog.models import Post,Category,comment
from django_summernote.admin import SummernoteModelAdmin

# @admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'cerated_date'
    empty_value_display = "-empty-"
    list_display = ["title","author",'login_required',"counted_views","status","publish_date","cerated_date"]
    list_filter=['status',"author"]
    ordering = ["cerated_date"]
    search_fields = ["title","content"]
    summernote_fields = ('content',)

class commentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ["name","post","approved","created_date"]
    list_filter=['post',"approved"]
    search_fields = ["name","post"]

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(comment,commentAdmin)
# Register your models here.
