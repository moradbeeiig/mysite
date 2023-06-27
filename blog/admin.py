from django.contrib import admin
from blog.models import Post

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'cerated_date'
    empty_value_display = "-empty-"
    list_display = ["title","author","counted_views","status","publish_date","cerated_date"]
    list_filter=['status',"author"]
    ordering = ["cerated_date"]
    search_fields = ["title","content"]

admin.site.register(Post,PostAdmin)

# Register your models here.
