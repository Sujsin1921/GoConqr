from django.contrib import admin

# Register your models here.
from .models import course
@admin.register(course)
class courceadmin(admin.ModelAdmin):
    list_display=('id','title','category','language','level','technology','description','doc_link','link','followup') 

from .models import userprofill
@admin.register(userprofill)
class courceadmin(admin.ModelAdmin):
    list_display=('id','name','email','background','category','language','level','technology') 