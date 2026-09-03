from django.shortcuts import render

def login_view(request):
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')