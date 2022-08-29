from socket import fromshare
from django import forms
#from .models import Board
from board.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents',)
        exclude = ('writer',)