from curses.ascii import HT
import re
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World!')
