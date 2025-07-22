from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sum(request):
    a = 5
    b = 6
    return HttpResponse(f"{a+b}")

def fullname(request):
    first_name = "Ali"
    last_name = "Rezaei"
    return HttpResponse (f'Your fullname is: "{first_name} {last_name}"')

def avg (request):
    nums = [12,20,15]
    sum = nums[0] + nums[1] + nums[2]
    return HttpResponse(f"Average = {sum/3}")

def power(request):
    num = 5
    return HttpResponse(f"Result = {num*num}")

def evenNum(request):
    num = 35
    evens =[]
    for n in range(1,num):
        if n%2 == 0:
            evens.append(str(n))
    result ='-'.join(evens)
    return HttpResponse(f"Result = {result}") 


