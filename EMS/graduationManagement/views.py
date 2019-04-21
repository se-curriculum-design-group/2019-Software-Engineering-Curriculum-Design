from django.shortcuts import render, redirect
def edit_title(request):
    return render(request, 'edit_title.html')
def view_titles(request):
    return render(request,'view_titles.html')