from django.shortcuts import render
from django.http import HttpResponse
# normal django view
def home (request):
    return HttpResponse('Hello world')
