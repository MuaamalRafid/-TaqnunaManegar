from django.shortcuts import render

from staff.models import Employee, Teams
from .forms import EmployeeForm, TeamsForm


def main(request):
   
    return render(request,'staff/index.html')

def empoinput(request):
    context={
     'form':EmployeeForm,
     'employee':Employee.objects.all(),
     'teams':Teams.objects.all()
   }  
    if request.method == 'POST':
     emdata = EmployeeForm(request.POST)
     if emdata.is_valid:
       emdata.save()
       
     
    return render(request,'staff/empoinput.html',context)

def teams(request):
    if request.method == 'POST':
      temdata = TeamsForm(request.POST)
      if temdata.is_valid:
        temdata.save()
    return render(request,'staff/teams.html',{'team':TeamsForm})

