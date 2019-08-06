from django.forms import CharField, Form, ModelForm, PasswordInput  # ... Others?
from photogur.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']


class LoginForm(Form):
    class Meta:
        username = CharField(label="User Name", max_length=64)
        password = CharField(widget=PasswordInput())

