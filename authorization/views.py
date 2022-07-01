from django.shortcuts import render


def auth(request):
    
    return render(request, 'authorization/auth.html')

def reg(request):
    return render(request, 'authorization/reg.html')

def log(request):
    return render(request, 'authorization/log.html')