from django.contrib import admin
from .models import post

class adminPost(admin.ModelAdmin):
    list_display = ["title"]
    list_filter =  ["publishingDate"]
    search_fields = ["title","text"]
    class Meta:
        model = post
# Register your models here.
admin.site.register(post)