"""photogur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #Needed to get the Admin section.
from django.urls import path
from photogur import views #Needed to refer to pages, redirects.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('pictures/', views.pictures_page, name="show_all"),  # Shows all pictures.

    path('accounts/login/', views.login_view, name="login"),
    path('accounts/logout/', views.logout_view, name="logout"),
    path('accounts/signup/', views.signup, name='signup'),

    path('pictures/<int:picture_id>', views.picture_details, name='picture_details'),  # Shows 1 specific picture.
    path('pictures/<int:picture_id>/edit', views.picture_edit, name='picture_edit'),  # Edits current picture, if owner.
    path('pictures/<int:picture_id>/comments/new', views.new_comment, name='new_comment'),  # Adds a new comment to current picture

    path('pictures/new', views.new_picture_form, name='new_picture_form'),  # Either renders a form to create a new picture, or saves a new picture.   
    path('pictures/search', views.picture_search, name='picture_search'),  # Searches for picture based on query.
    
    


]
