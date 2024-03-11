from django.shortcuts import render
from django.shortcuts import render, redirect
from Customers.forms import CustomerForm
from Customers.forms import RegisterForm
from django.contrib import messages



def index(request):
    form = RegisterForm()
    if request.method == 'POST':
     form = RegisterForm(request.POST)
    if form.is_valid():
     form.save()
    else:
        form= RegisterForm()
        messages.success(request, '')()
    return redirect('index')


def register(request):
    form = RegisterForm()
    return render(request, 'register.html',{"form": form})



def Admin(request):
    form = CustomerForm()
    return render(request, 'admin.html',{"form":form})


def Contact(request):
    form = CustomerForm()
    return render(request, 'Contact.html',{"form":form})


def teacher(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
    else:
         form = RegisterForm()
    return render(request, 'teacher.html',{"form":form})