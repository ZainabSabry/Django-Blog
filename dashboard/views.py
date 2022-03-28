from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from category.models import Category, Post
from .form import EditPostForm, CategoryForm



# Create your views here.
def allUsers(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        st = User.objects.all()
        context = {"all_users": st, "categories": categories}
        return render(request, 'dashboard/manage-users.html', context)
    return redirect('all-users')
    


def showUser(request, userid):
    userID = User.objects.get(id=userid)
    context = {'id': userID}
    return render(request, 'dashboard/show-user.html', context)
    


def delUser(request, userid):
    user = User.objects.get(id=userid)
    user.delete()
    return redirect('all-users')
    

def blockUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_active = False
    user.save()
    return redirect('all-users')
    


def unblockUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_active = True
    user.save()
    return redirect('all-users')
    


def adminUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return redirect('all-users')
    

def unadminUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_superuser = False
    user.is_staff = False
    user.save()
    return redirect('all-users')
    


def all_Posts(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        post = Post.objects.all()
        context = {"all_posts": post, 'categories': categories}
        return render(request, 'dashboard/manage-posts.html', context)
    return redirect('all-posts')
    

def addPost(request):
    if request.user.is_authenticated:
        form = EditPostForm()
        categories = Category.objects.all()
        if request.method=='POST':
            form = EditPostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('all-posts')
            else:
                form = EditPostForm()

        context = {
            'form': form,
            'categories': categories,
            }
        return render(request, 'dashboard/addpost.html', context)
    else:
        return redirect('all-posts')
    

def postEdit(request, postID):
    if request.user.is_authenticated:
        post = Post.objects.get(id = postID)
        form = EditPostForm(instance=post)
        categories = Category.objects.all()
        if request.method=='POST':
            form = EditPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('all-posts')
            else:
                form = EditPostForm(instance=post)

        context = {
            'post': post, 
            'form': form,
            'categories': categories,
            }
        return render(request, 'dashboard/editpost.html', context)
    else:
        return redirect('all-posts')
        


def postDelete(request, postID):
    if request.user.is_authenticated and request.user.is_superuser:
        post = Post.objects.get(id=postID)
        post.delete()
    return redirect('all-posts')
    


def allCats(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        cat = Category.objects.all()
        context = {"all_cats": cat, 'categories': categories}
        return render(request, 'dashboard/manage-cat.html', context)
    return redirect('all-cats')

def delCat(request, catid):
    if request.user.is_authenticated:
        cat = Category.objects.get(id=catid)
        cat.delete()
        return redirect('all-cats')
    return redirect('all-cats')

def addCat(request):
    if request.user.is_authenticated and request.user.is_superuser:
        form = CategoryForm()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('all-cats')
        context = {'form': form}
        return render(request, 'dashboard/addCat.html', context)
    else:
        return redirect('all-cats')

def editCat(request, catid):
    if request.user.is_authenticated:
        cat = Category.objects.get(id = catid)
        form = CategoryForm(instance=cat)  
        if request.method=='POST':
            form = CategoryForm(request.POST, instance=cat)
            if form.is_valid():
                form.save()
                return redirect('all-cats')
            else:
                form = CategoryForm(instance=cat)

        context = {
         
            'form': form,
          
            }
        return render(request, 'dashboard/edit-cat.html', context)
    else:
        return redirect('all-cats')



        
