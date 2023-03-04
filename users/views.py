from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from users.form import UserForm


# Create your views here.

def home(request):
    error= '' 
    print('home')
    if request.method == "POST":
        print(request)
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username= username,password = password)
        if user is not None:
            login(request, user)
            if user.is_salaries:
                return redirect('salaries')
            elif user.is_RH_Campagnies:
                return redirect('RH_Campagnies')
            else:
                return redirect('admin_WebApps')
        else:
            print('error')
            error="password ou username est inccorect"
    return render(request, 'login.html', {'error':error})

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form=UserForm(data= request.POST)
        print('is valide ?')
        if form.is_valid():
            print('to save')
            form.save()
            print('saved')
            return redirect('home')
    return render(request, 'register.html', {'form': form})



def salaries(request):
    return render(request, 'salaries.html')

def RH_Campagnies(request):
    return render(request, 'RH_Campagnies.html')

def admin_WebApps(request):
    return render(request, 'admin_WebApps.html')