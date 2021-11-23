from django.http import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):

    if request.method =='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
        user.save()
        print("user created")
        return redirect('/')

    else:
        return render(request,'register.html')


def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect("/admin")

    else:
        return render(request,'login.html')