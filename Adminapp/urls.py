from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.adminHome,name='admin_home'),
    path('adminProfile/',views.adminProfile,name='admin_profile'),

    path('delete_User/<str:user_name>/',views.deleteUser, name = 'deleteUser'),

    path('blog_Users/',views.blogUsers,name='blogUsers'),

    path('user_blogs/<str:user_name>/',views.viewUserBlogs,name='userBlogs_admin'),

    path('block_User/<str:user_name>/',views.BlockUser,name='blockUser'),
    path('unblock_User/<str:user_name>/', views.unBlockUser, name='unblockUser'),

    path('blockBlogs/<int:blog_id>/',views.blockBlogs, name = 'blockBlogs'),
    path('unblockBlogs/<int:blog_id>/',views.unblockBlogs, name = 'unblockBlogs'),

    path('delete_Blog/<int:blog_id>/',views.delBlog, name = 'delBlogs'),


]