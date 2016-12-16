from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
# from .models import User, Book, Review

def index(request):
    return render(request, 'coolapp/index.html')
