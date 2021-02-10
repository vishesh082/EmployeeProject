from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . forms import EmployeeForm
from . models import EmployeeModel

# Create your views here.


def index(request):
    if request.method == "POST":
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
          fm.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def display_(request):
    user = EmployeeModel.objects.all()
    return render(request, 'view.html', {'form': user})


def delete_(request,id):
    user = EmployeeModel.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect('/')