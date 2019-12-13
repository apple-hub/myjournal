from django import forms

from .models import Journal, Comment

class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
