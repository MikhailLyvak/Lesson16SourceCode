from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomUserCreationForm, LoginForm
from users.models import CustomUser

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            
            if user is not None:
                login(request, user)
                return redirect("app_to_buy_list:item-list")
            else:
                return redirect('users:login')
        
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'auth/register.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = form.get_authenticated_user()
            
            if user is not None:
                login(request, user)
                return redirect("app_to_buy_list:item-list")
    
    else:
        form = LoginForm()
        
    return render(request, 'auth/login.html', {"form": form})


def logout_view(requset):
    logout(requset)
    return redirect('users:login')
            