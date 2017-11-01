# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def show(request, blog_number):
    return HttpResponse(("placeholder to display blog {}".format(blog_number)))

def edit(request, blog_number):
    return HttpResponse("placeholder to edit blog {}".format(blog_number))

def destroy(request, blog_number):
    return redirect('/')