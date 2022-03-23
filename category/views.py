from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
import os
from taggit.models import Tag
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse



# Create your views here.

#All posts of a specific category
def allPosts(request, category=None, tag_slug=None):
    posts = Post.objects.filter(categ=category)
    categories = Category.objects.all()


    #Adding Pagination to avoid having all posts in one page
    paginator = Paginator(posts, 5) # 5 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    # Adding tags for each post
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])

    context = {'posts': posts, page: 'pages', 'tag': tag, 'categories': categories}
    return render(request, 'category/all_posts.html', context)


#View of a single post
def postDetails(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()

    post_url = request.POST.get('post_url')


    # List of all comments
    comments = post.comments.filter(proper=True)
    new_comment = None
    comment_form = None

    if request.method == 'POST':

        # first check if user is authenticated or not
        
        # a new comment is added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post 
            new_comment.save()
            #redirect to same page but focus on comment
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()

    context = {'post': post, 'comments': comments, 'comment_form': comment_form, 'categories': categories}
    return render(request, 'category/post_details.html', context)



