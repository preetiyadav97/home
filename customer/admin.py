from django.contrib import admin
from .models import Employee_detail

# Register your models here.
class Employee_detailAdmin(admin.ModelAdmin):
    model=Employee_detail
    list_display=['name','department','email','number']
    
admin.site.register(Employee_detail,Employee_detailAdmin)
