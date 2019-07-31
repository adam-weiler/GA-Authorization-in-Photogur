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

def create_comment(request):
    new_comment = Comment() #Instantiates a new_comment.
    picture_id = request.POST['picture'] #Retrieves the picture id from the POST request. (It's hidden.)
    picture = Picture.objects.get(pk=picture_id) #Gets the entire picture object.

    new_comment.name = request.POST['name'] #Retrieves the name from the POST request.
    new_comment.message = request.POST['message'] #Retrieves the message from the POST request.
    # breakpoint()
    new_comment.picture = picture #Sets the foreign key as the picture object.
    
    new_comment.save() #Saves the new_comment to the database.
    # return HttpResponseRedirect('/picture/') #Why does this redirect instead of render?

    context = {'picture': picture}
    response = render(request, 'picture.html', context)
    return HttpResponse(response)


# picture = Picture.objects.get(pk=id)

    #redirect back to picture page      Don't render