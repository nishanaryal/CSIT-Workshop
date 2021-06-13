from django.contrib import admin
from hospitals.models import DonatePlasma, OtherRequest, RequestBed

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','streetAddress','city','state','contactNo', 'action_status','seenStatus', 'requestOn')
    list_filter = ['action_status','seenStatus','state']
    search_fields = ['full_name']
    

admin.site.register(RequestBed, AuthorAdmin)
admin.site.register(DonatePlasma, AuthorAdmin)
admin.site.register(OtherRequest, AuthorAdmin)
