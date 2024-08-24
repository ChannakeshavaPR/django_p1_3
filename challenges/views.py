from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse("This january!!")


def February(request):
    return HttpResponse("This February!!")


def March(request):
    return HttpResponse("This March!!")


def monthly_challenge(request, month):
    if month == "january":
        return HttpResponse("This january!!")
    elif month == "february":
        return HttpResponse("This February!!")
    elif month == "march":
        return HttpResponse("This march!!")
    elif month == "april":
        return HttpResponse("This april!!")
    else:
        return HttpResponseNotFound("this month is not supported")
