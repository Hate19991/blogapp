from django.contrib import admin
from .models import *

class NotesAdmin(admin.ModelAdmin):
    list_display = ["id","text", "title","created_at","image","created_by"]
    search_fields = ["id" ,"text","title","created_at","image","created_by"]
    list_filter = ['created_at']
    readonly_fields = ['created_at','created_by']
    
admin.site.register(Notes , NotesAdmin)
# Register your models here.
