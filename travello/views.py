from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination() 
    dest1.name='Mumbai'
    dest1.price=700
    dest1.desc='City that never sleep'


    dest2 = Destination() 
    dest2.name='Gulaothi'
    dest2.price=350
    dest2.desc='My Home Town'

    dest3 = Destination() 
    dest3.name='Delhi'
    dest3.price=1000
    dest3.desc='Capital of India'

    dests = [ dest1, dest2, dest3 ]

    return render(request,'index.html',{'dests': dests})

    #return render(request,'index.html',{'dest1': dest1,'dest2': dest2, 'dest3': dest3})