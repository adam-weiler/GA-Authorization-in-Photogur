from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from photogur.forms import CommentForm, LoginForm, PictureForm  # ... others?
from photogur.models import Picture, Comment


def pictures_page(request): #Loads all the pictures.
    return render(request, 'pictures.html', { 
        'gallery_images': Picture.objects.all(), 
        'gallery_comments': Comment.objects.all() 
    })


def picture_show(request, id): #Loads an individual picture.
    picture = Picture.objects.get(pk=id)

    return render(request, 'picture.html', {
        'picture': picture, 
        "form": CommentForm(instance=picture)
    })


def picture_search(request): #Loads the search results.
    query = request.GET['query']
    search_results = Picture.objects.filter(  # Checks if artist, title, or URL contains word.
        artist__contains=query
        ).union(
            Picture.objects.filter(title__contains=query)
        ).union(
            Picture.objects.filter(url__contains=query)
        )

    return render(request, 'picture_search.html', {
        'pictures': search_results, 
        'query': query
    })


def create_comment(request, picture_id): #Saving a comment in the database.
    # breakpoint()
    # picture_id = request.POST['picture'] #Retrieves the picture id from the POST request.
    # breakpoint()
    picture = Picture.objects.get(pk=picture_id) #Gets the entire picture object.
    
    form = CommentForm(request.POST)
    new_comment = form.save(commit=False)
    
    new_comment.picture = picture #Adding this line
    new_comment.save()

    context = {'picture':picture}
    # return redirect(reverse('pictures/' + picture_id))

    # return render(request, "picture.html", context) #This is returning to the image page but the form disappears.
  

    # return HttpResponseRedirect('/pictures')
    return HttpResponseRedirect(f'/pictures/{picture_id}')  #Why should this redirect instead of render?


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

    return render(request, 'registration/login.html', {
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

    return render(request, 'registration/signup.html', {
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

