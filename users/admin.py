from django.contrib import admin
from .models import *

# Register your models here.
class IMuserAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name",)    
admin.site.register(IMUser,IMuserAdmin)

class CohortAdmin(admin.ModelAdmin):
    list_display= ("name", )
admin.site.register(Cohort,CohortAdmin)
