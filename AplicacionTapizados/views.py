from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Vlogin (request): # template
    return render(request, "Maqueta/login.html")

def VloginAdmin (request): # template
    return render(request, "Maqueta/loginAdmin.html")