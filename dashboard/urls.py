from django.urls import path
from . import  views


urlpatterns = [
  #Manges Users Urls
  path('all-users/', views.allUsers, name='all-users'),
  path('show-user/<userid>', views.showUser, name='show-user'),
  path('del-user/<userid>', views.delUser, name='del-user'),
  path('block-user/<userid>', views.blockUser, name='block-user'),
  path('unblock-user/<userid>', views.unblockUser, name='unblock-user'),
  path('admin-user/<userid>', views.adminUser, name='admin-user'),
  path('unadmin-user/<userid>', views.unadminUser, name='unadmin-user'),

  #Manges Posts Urls
  path('all-posts/', views.all_Posts , name='all-posts'),
  path('add-post/', views.addPost, name='add-post'),

  # Manges Categories Urls
  path('all-cats/', views.allCats, name='all-cats'),
  path('addCat/', views.addCat, name='add-cat'),
  path('editCat/<catid>', views.editCat, name='edit-cat'),
  path('del-cat/<catid>', views.delCat, name='delete-cat'),

  path('editpost/<postID>', views.postEdit, name="editpost"),
  path('deletepost/<postID>', views.postDelete, name="deletepost"),
 

  ]
  
