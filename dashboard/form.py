from category.models import Post, Category
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'image', 'author', 'content', 'publish_date', 'categ', 'tags')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'image', 'author', 'content', 'publish_date', 'categ', 'tags')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)


