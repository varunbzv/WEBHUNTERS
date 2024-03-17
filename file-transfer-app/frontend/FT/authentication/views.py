from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method== "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(username , email ,pass1)
        myuser.save()

        messages.success(request ,"Signed Up")

        return redirect('signin')


    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username , password=pass1)
        if user is not None:
            login(request, user)
            username = user.username
            return render(request , "authentication/index.html" , {'username': username})
        else:
            messages.error(request ,"check username and password")
            return redirect('signout')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out")
    return redirect('home')

def upload(request):
    return render(request, "authentication/upload.html")




