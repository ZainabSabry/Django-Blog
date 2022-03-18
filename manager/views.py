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
        lock_user(user)
        log(request.user.username+" locked " + user.username+".")
        return HttpResponseRedirect("redirect path")
    else:
        return HttpResponseRedirect("redirect path")


def Admin_unlock_user(request, id):

    ### unlock a specific user so he can login again
    
    if(is_authorized_admin(request)):
        user = User.objects.get(pk=id)
        unlock_user(user)
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


