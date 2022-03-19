from django.shortcuts import render
from category.models import Category , Post
# from .models import Student
# Create your views here.

def landing_page_components(request):
    categories = Category.objects.all()
    posts = Post.objects.all()[:5]
    context = {'categories' : categories , 'posts' : posts}
    return render(request,'landing_page/all.html',context)

