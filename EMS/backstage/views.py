import os
from django.shortcuts import render, redirect


def welcome(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')
    pass


def register(request):
    return render(request, 'register.html')
    pass


def logout(request):
    pass
