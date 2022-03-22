from django.shortcuts import render , redirect
from category.models import Category, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(redirect_field_name=None, login_url='/signup_in/login/')
# @login_required
def landing_page_components(request):
    categories = Category.objects.all()
    posts = Post.objects.all()[:5]
    context = {'categories': categories, 'posts': posts}
    return render(request, 'landing_page/all.html', context)

@login_required
def post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'landing_page/post.html', context)

def sub(request,cat):
    category = Category.objects.get(id=cat)
    if request.method == 'POST':
        if category.is_subscribed == False:
            category.is_subscribed = True
            return redirect('../../landing_page/home/')
        else:
            category.is_subscribed = False
            return redirect('../../landing_page/home/')
    # return redirect('home')

