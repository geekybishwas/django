from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method=="POST":
        # It pass 
        # pass
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # If user is not none the logged the user
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('There was an error logging in'))
            return redirect('login')
    else:
        return render(request,'auth/login.html',{})
