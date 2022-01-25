from django.shortcuts import render,redirect
from .models import Employee
from .forms import Employee_form
# Create your views here.
def retrive_view(request):
    emp_list=Employee.objects.all().order_by("eno")
    return render(request,"retrive.html",{"emp_list":emp_list})

def create_view(request):
    form=Employee_form()
    if request.method=="POST":
        form=Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request,"create.html",{"form":form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/home")

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=Employee_form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("/home")

    return render(request,"update.html",{"employee":employee})






