from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def newlog(request):
    
    return render(request,'newlog.html')

def update(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        print(name,email,'<------')
        return render(request,'login.html')
    else:
        return render(request,'newlog.html')