from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")


def about(request):
    return HttpResponse("About")
