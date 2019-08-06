from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect #Needed to return an HttpResponse.
from django.urls import reverse
from django.shortcuts import redirect, render #Needed to render the page.
from photogur.forms import CommentForm, LoginForm, PictureForm  # ... others?
from photogur.models import Picture, Comment #Importing the classes from models.py file.


def pictures_page(request): #Loads all the pictures.
    return render(request, 'pictures.html', { 
        'gallery_images': Picture.objects.all(), 
        'gallery_comments': Comment.objects.all() 
    })


def picture_show(request, id): #Loads an individual picture. #This is the Edit function.
    picture = Picture.objects.get(pk=id)

    return render(request, 'picture.html', {
        'picture': picture, 
        "form": CommentForm(instance=picture)
    })


def picture_search(request): #Loads the search results.
    query = request.GET['query']
    # search_results = Picture.objects.filter(artist=query)
    # matches = 'artist' | 'title' | 'url'
    # search_results = Picture.objects.filter(Q(artist__icontains=query) | Q(title__icontains=query) | Q(url__icontains=query))
    search_results = Picture.objects.filter(  # Checks if artist, title, or URL contains word.
        artist__contains=query
        ).union(
            Picture.objects.filter(title__contains=query)
        ).union(
            Picture.objects.filter(url__contains=query)
        )

    context = {'pictures': search_results, 'query': query}

    #Adding these things
    response = render(request, 'picture_search.html', context)
    return HttpResponse(response)




def create_comment(request): #Saving a comment in the database.
    # # new_comment = Comment() #Instantiates a new_comment.
    picture_id = request.POST['picture'] #Retrieves the picture id from the POST request. (It's hidden.)
    # breakpoint()
    picture = Picture.objects.get(pk=picture_id) #Gets the entire picture object.
    
    # # new_comment.name = request.POST['name'] #Retrieves the name from the POST request.
    # # new_comment.message = request.POST['message'] #Retrieves the message from the POST request.
    # # breakpoint()
    # # new_comment.picture = picture #Sets the foreign key as the picture object.
    
    # # new_comment.save() #Saves the new_comment to the database.
    

    # form = CommentForm(request.POST)
    # # breakpoint()
    # # form.save()

    # context = {'picture': picture}
    # response = render(request, 'picture.html', context)
    # return HttpResponse(response) #Why should this redirect instead of render?

    # # return HttpResponseRedirect(response) #Why should this redirect instead of render?

    form = CommentForm(request.POST)
    new_comment = form.save(commit=False)
    
    new_comment.picture = picture #Adding this line
    new_comment.save()
    # return HttpResponseRedirect('/')
    context = {'picture':picture}
    # return redirect(reverse('pictures/' + picture_id))

    # return render(request, "picture.html", context) #This is returning to the image page but the form disappears.
    return HttpResponseRedirect(f'/picture/{picture_id}') #Why should this redirect instead of render?


def login_view(request):  
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/pictures')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/pictures')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/pictures')


@login_required
def new_picture(request):
    form = PictureForm(request.POST)

    if form.is_valid():
        new_picture = form.save(commit=False)
        new_picture.user = request.user
        new_picture.save()

        return redirect(reverse('show_all'))
    else:  # Else sends user back to picture_form page.
        return render(request,'picture_form.html', {
            'form': form
        })

    #save to database


    # render pictureform



