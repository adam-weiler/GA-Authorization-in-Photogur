from django.http import HttpResponse #Needed to return an HttpResponse.
from django.shortcuts import render #Needed to render the page.
from photogur.models import Picture, Comment #Importing the classes from models.py file.

def pictures_page(request): # Redirects to http://localhost:8000/home/
    context = { 'gallery_images': Picture.objects.all(), 'gallery_comments': Comment.objects.all() }

    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}

    response = render(request, 'picture.html', context)
    return HttpResponse(response)

def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}

    #Adding these things




    response = render(request, 'picture_search.html', context)
    return HttpResponse(response)
