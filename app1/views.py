from django.shortcuts import render,redirect
from . forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    
    return render(request,"app1/home.html")

def register(request):
    if request.method =='POST':
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'app1.backend.EmailAuthBackend'  # Set this based on your custom backend
            login(request,user)
            return redirect("home_page")

    else:
        form =CustomUserCreationForm()
    context ={'form':form}
    return render(request,'app1/register.html',context)

def login_page(request):

    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = authenticate(request, username=email, password=password)
        print(user)
        
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('home_page')  # Redirect to the home page (or any other page)
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid email or password")
            print('invalid')
    return render(request,'app1/loginp.html')