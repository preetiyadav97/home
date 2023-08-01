from django.shortcuts import render,HttpResponse,redirect
from customer.models import Employee_detail

# Create your views here.
def first(request):
    show=Employee_detail.objects.all()
    data={'show' : show}
    return render (request,'index.html',data)
    
def Update(request,uq):
    dat=Employee_detail.objects.get(id=uq)
    if request.method == 'POST':
        name=request.POST.get("fname")
        department=request.POST.get("dept")
        
        email=request.POST.get("email")
        
        number=request.POST.get("number")
        
        dat.name=name
        dat.department=department
        dat.email=email
        dat.number=number
        dat.save()
        return redirect('first')
    
    col={"dat":dat}
    return render (request,'update.html',col)
        
    
def Create(request):
    if request.method == 'POST':
        name=request.POST["fname"]
        department=request.POST["dept"]
        
        email=request.POST["email"]
        
        number=request.POST["number"]
        
        d=Employee_detail(name=name,department=department,email=email,number=number)
        d.save()
        return redirect('first')
     
    return render (request,'create.html')

def Delete(request,uq):
    dat=Employee_detail.objects.get(id=uq)
    dat.delete()
    show=Employee_detail.objects.all()
    data={'show' : show}
    return render (request,'index.html',data)
    
    