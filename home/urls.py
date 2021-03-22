from django.urls import path
from . import views  

urlpatterns=[
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('newlog',views.newlog, name='newlog'),
    path('update',views.update, name='update'),
    path('signupComplete',views.signupComplete, name='signupComplete'),
    
]