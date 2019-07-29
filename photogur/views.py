from django.http import HttpResponse #Needed to return an HttpResponse.
from django.shortcuts import render #Needed to render the page.
from photogur.models import Picture, Comment #Importing the classes from models.py file.

def pictures_page(request): # Redirects to http://localhost:8000/home/
    context = { 'gallery_images': Picture.objects.all(), 'gallery_comments': Comment.objects.all() }

    # context = { 'pictures': 7 }

    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}

    response = render(request, 'picture.html', context)
    return HttpResponse(response)