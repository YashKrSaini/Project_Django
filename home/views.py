from django.shortcuts import render
from home.models import userData

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginResponse(request):
    if (request.method=="POST"):
        recv_email=request.POST['email_id']
        recv_passWord=request.POST['passWord']
        for user in userData.objects.all() :
            print('---------------------->',user.name)
            if (user.email==recv_email):
                if (user.passWord==recv_passWord):
                    # LOgin Succesfully
                    return render(request,'loginResponse.html',{'status':'Succesfully',})
                else:
                    # PassWord Incorrect
                    return render(request,'loginResponse.html',{'status':'Failed','reason':'Incorrect Password'})
        return render(request,'loginResponse.html',{'status':'Failed','reason':'Incorrect Email Id'})


def newlog(request):
    
    return render(request,'newlog.html')

def update(request):
    if request.method=="POST":
        name=request.POST['id']
        email=request.POST['email_id']
        # print(name,email,'<------') # Working Properly
        return render(request,'login.html')
    else:
        return render(request,'newlog.html')

def signupComplete(request):
    if request.method=="POST":
        name=request.POST['id']
        passWord=request.POST['pass']
        rePass=request.POST['repass']
        email=request.POST['email_id']
        dob=request.POST['dob']
        image=request.POST['image']
        if (passWord==rePass and len(rePass)!=0):
            ins =  userData(name=name,email=email,passWord=passWord ,dob=dob,image=image)
            ins.save()
            try :
                name=str(name.split()[0])
            except :
                pass
            return render(request,'signupComplete.html',{'name':name})
        else:
            return render(request,'signupFailed.html')
            