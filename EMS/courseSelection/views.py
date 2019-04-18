from django.shortcuts import render
import os
from django.shortcuts import render, redirect
from . import models
from django.contrib import auth
from random import choice
from django.contrib.auth.hashers import make_password, check_password
import datetime
# 邮件模块
from django.conf import settings
from django.core import mail

# Create your views here.
def courseSelection(request):
    return render(request,"courseSelectionH5/courseSelection.html")

def courseSelecting(request):
    return render(request,"courseSelectionH5/courseSelect.html")
def personalTable(request):
    return render(request,"courseSelectionH5/personalTable.html")

