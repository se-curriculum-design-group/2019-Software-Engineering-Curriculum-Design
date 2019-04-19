from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, 'graduationManagement/welcome.html')


def func(request):
    return HttpResponse("func")
