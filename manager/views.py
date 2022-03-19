from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import Profile
from django.contrib.auth.models import User
from users.logger import log
from users.util_funcs import *

def Admin_lock_user(request, id):

  ### lock a specific user not to be able to login again but his account still exist
   
    if(is_authorized_admin(request)):
        user = User.objects.get(pk=id)
        user.is_locked = True
    	user.save()
        log(request.user.username+" locked " + user.username+".")
        return HttpResponseRedirect("redirect path")
    else:
        return HttpResponseRedirect("redirect path")


def Admin_unlock_user(request, id):

    ### unlock a specific user so he can login again
    
    if(is_authorized_admin(request)):
        user = User.objects.get(pk=id)
        user.is_locked = False
    	user.save()
        log(request.user.username+" unlocked " + user.username+".")
        return HttpResponseRedirect("redirect path")
    else:
        return HttpResponseRedirect("redirect path")
        
       
 
def is_authorized_admin(request):

  ### check if user is authorized admin
  
    if(request.user.is_authenticated):
        if(request.user.is_staff):
            return True
    return False    


def manager_show_user(request, id):

    ### show information about specific user 
 
    if(is_authorized_admin(request)):
        user = User.objects.get(pk=id)
        return render(request, "show_user.html", {"user": user})
    else:
        return HttpResponseRedirect("redirect path")


def promote_user(request, id):

    ### promote a specific user to become an admin 
    
    if(is_authorized_admin(request)):
        user = User.objects.get(pk=id)
        user.is_staff = True
    	user.save()
        log(request.user.username+" promoted " + user.username+".")
        return HttpResponseRedirect("redirect path")
    else:
        return HttpResponseRedirect("/")


def demote_admin(request, id):

    ### demote a specific admin to become a normal user again
   
    current_user = request.user
    if(is_authorized_admin(request)):
        if(current_user.is_staffuser):
            user = User.objects.get(pk=id)
            user.is_staff = False
            user.save()
            log(current_user.username+" demoted " + user.username+".")
        return HttpResponseRedirect("redirect path")
    else:
        return HttpResponseRedirect("redirect path")




def posts(request):
    if(is_authorized_admin(request)):
        posts = Post.objects.all()
        categories = Category.objects.all()
        context = {'posts': posts, 'categories': categories}
        return render(request, 'redirect path', context)
    else:
        return HttpResponseRedirect("redirect path")


def post_delete(request, post_id):
    if(is_authorized_admin(request)):
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect('redirect path')
    else:
        return HttpResponseRedirect("redirect path")


def add_category(request):
    if(is_authorized_admin(request)):
        form = CategoryForm()
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                log("form is valid")
                return HttpResponseRedirect('redirect path')
        else:
            context = {"pt_form": form}
            return render(request, "redirect path", context)
    else:
        return HttpResponseRedirect("redirect path")


def delete_category(request, cat_id):
    if(is_authorized_admin(request)):
        category = Category.objects.get(id=cat_id)
        category.delete()
        return HttpResponseRedirect('redirect path')
    else:
        return HttpResponseRedirect("redirect path")

