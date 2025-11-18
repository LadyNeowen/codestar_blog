"""
Forms for the blog application.

This module contains form classes used to handle user input related
to comments on blog posts.
"""


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    """
    Form for submitting a comment on a blog post.

    This form is based on the Comment model and includes only
    the 'body' field, allowing users to enter the text of their comment.
    """
    
    class Meta:
        model = Comment
        fields = ('body',)