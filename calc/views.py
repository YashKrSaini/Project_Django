from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request,'home.html',{'name':'Aashu'})# Dynamic Coding

def prob(request):
    return render(request,"prob.html")

def add(request):
    try:
        val1=float(request.POST['num1'])
        val2=float(request.POST['num2'])
        res = val1 + val2
        return render(request,"result.html",{'result':res})
    except:
        return render(request,"prob.html")

def new(request):
    name=str(request.POST['name'])
    dob=str(request.POST['date'])
    res=name+str(' ')+dob
    return HttpResponse(res)
