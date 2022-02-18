from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import AuthenticationForm

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # form = AuthenticationForm(request=request,data=request.POST)
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                print(email, username, password)
                # user = authenticate(request,email=email,password=password)
                user1 = authenticate(email=email,password=password)
                print('user1: ', user1)
                user2 = authenticate(username=username,password=password)
                print('user2: ', user2)
                # print(user.username)
                if user1 is not None:
                    login(request,user1)
                    return redirect('/')
                else:
                    login(request,user2)
                    return redirect('/')
                    
    
        form = AuthenticationForm()        
        context ={'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context={'form': form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')

