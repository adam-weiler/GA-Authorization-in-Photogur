from django.forms import CharField, ModelForm, PasswordInput  # ... Others?
from photogur.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']


class LoginForm(ModelForm):
    class Meta:
        username = CharField(label="User Name", max_length=64)
        password = CharField(widget=PasswordInput())

