from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def HOME(request):
    return render(request,'margins.html')
