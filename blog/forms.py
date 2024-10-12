from pyexpat import model
from django import forms
from .models import PostModel, CommentPost

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['content']   
        
