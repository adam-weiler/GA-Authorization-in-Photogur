from django.contrib import admin
from photogur.models import Picture, Comment #Importing the classes from models.py file.

admin.site.register(Picture)
admin.site.register(Comment)
