from django.shortcuts import render

# Create your views here.

def signup(request):
    
    return render(request, 'accounts/signup.html')

def signin(request):
    return render(request, 'accounts/signin.html')

def success(request):
    return render(request, 'accounts/success.html')

def token_send(request):
    return render(request, 'accounts/token_send.html')