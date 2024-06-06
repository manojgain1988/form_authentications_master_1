from django.contrib import admin
from .models import contactModel
# Register your models here.

class contactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','contact','city']
    
admin.site.register(contactModel, contactModelAdmin)