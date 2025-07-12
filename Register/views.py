from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fullname (request):
    fname = input("Enter your first name:")
    lname = input("Enter your last name:")
    return HttpResponse (f'Your fullname is: {fname} {lname}')

# or 

# def fullname (request):
#     return HttpResponse ('Your fullname is: Hadiqe mahdavi')
