from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import  User
from accounts.forms import  registerForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView, DeleteView

def profile(request):
    return render(request, 'accounts/profile.html')

class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = registerForm
    success_url = reverse_lazy("login")

def userLogin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return render(request,'accounts/profile.html')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'accounts/login.html',{'form': form})

def userLogout(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')  

class UserUpdate(UpdateView):
    model = User
    template_name = 'accounts/edit.html'
    form_class = registerForm
    success_url = reverse_lazy('account.profile')

class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('category.index')