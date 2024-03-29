from django.forms import CharField, Form, ModelForm, PasswordInput  # ... Others?
from photogur.models import Comment, Picture


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'artist', 'url']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']


class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

