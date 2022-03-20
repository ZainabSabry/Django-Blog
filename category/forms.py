from django import forms 
from .models import Comment
from better_profanity import profanity

# Form for the comments
class CommentForm(forms.ModelForm):
    profanity.load_censor_words()
    class Meta:
        model = Comment
        fields = ('name', 'comment_title', 'comment_body')

    # override default form settings and adding bootstrap
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Please type your name', 'class': 'form-control'}
        self.fields['comment_title'].widget.attrs = {'placeholder': 'Type title', 'class': 'form-control'}
        self.fields['comment_body'].widget.attrs = {'placeholder': 'Comment here...', 'class': 'form-control', 'rows': '5'}
        