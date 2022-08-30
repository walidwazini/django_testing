from django.http import HTTPResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HTTPResponse('This works.')
