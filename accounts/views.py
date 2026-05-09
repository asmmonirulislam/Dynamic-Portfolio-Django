from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Invalid Credentials, Try Again!')
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

@require_POST
def logout_user(request):
    logout(request)
    messages.info(request, 'Logged Out')
    return redirect(request.META.get('HTTP_REFERER'))