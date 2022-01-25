from django.contrib import admin
from testApp.models import Employee
# Register your models here.
class Employee_admin(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddr"]
admin.site.register(Employee,Employee_admin)