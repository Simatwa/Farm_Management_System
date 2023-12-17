from django.shortcuts import render,redirect

# Create your views here.
def Mainpage(request):

    return render(request, 'homepage/home.html')

#views for the employees
from .employees_form import EmployeesForm
from .models import Employees

def Show_employees(request):
    employees = Employees.objects.filter(user=request.user)


    return render(request, 'homepage/showemployees.html', {'employees':employees})

def Add_employees(request):
    if request.method=='POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            employees= form.save(commit=False)
            employees.user = request.user

            form.save()

            return redirect('homepage:show-employees')
        
    else:
        form =EmployeesForm()
    return render(request, 'homepage/addemployees.html', {'form':form})

def Delete_employees(request, Eid):
    employees =Employees.objects.get(Eid=Eid)
    if request.method =='POST':
        employees.delete()
        return redirect('homepage:show-employees')
    
    return render(request, 'homepage/deleteemployees.html', {'employees':employees})

def Update_employees(request,Eid):
    employees = Employees.objects.get(Eid=Eid)
    form =EmployeesForm(request.POST, instance=employees)

    if form.is_valid():
        form.save()
        return redirect('homepage:show-employees')
    
    return render(request, 'homepage/updateemployees.html', {'employees':employees})