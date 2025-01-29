from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.userHome,name='user_home'),

    path('userProfile/',views.userProfile,name='user_profile'),

    path('addBlog',views.addBlog,name='addBlog'),

    path('BlogsActions/',views.BlogsActions,name='BlogsActions'),

    path('EditBlog/<int:blog_id>/',views.EditBlog,name='editBlog'),
    path('DeleteBlog/<int:blog_id>/',views.delBlog,name='deleteBlog'),

    path('AddComments/<int:blog_id>/',views.addComments,name='addComments'),
    path('BlogComments/<int:blog_id>/', views.blogComments, name ='blogComments'),
]