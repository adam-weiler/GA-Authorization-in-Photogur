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
    path('accounts/login/', views.login_view, name="login"),
    path('accounts/logout/', views.logout_view, name="logout"),
    path('pictures/', views.pictures_page, name="show_all"), #Page
    path('pictures/<int:picture_id>', views.picture_show, name='image_details'),
    path('pictures/<int:picture_id>/comments/new', views.create_comment, name='create_comment'),
    path('pictures/search', views.picture_search, name='picture_search'),
    path('accounts/signup/', views.signup, name='signup'),
    path('pictures/new', views.new_picture, name='new_picture'),  # Form to create a new picture.
]
