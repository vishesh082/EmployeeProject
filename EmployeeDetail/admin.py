from django.contrib import admin
from . models import EmployeeModel
# Register your models here.


class Employeeeadmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname','code']


admin.site.register(EmployeeModel, Employeeeadmin)
