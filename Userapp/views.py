
from django.contrib.auth.decorators import login_required
from .models import UserBlogs, BlogComments
from django.contrib import messages
from django.shortcuts import render, redirect
from Accountsapp.models import loginTable
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# from Userapp.forms import UpdateForm


# Create your views here.

def userHome(request):

    username = request.session['username']
    user = loginTable.objects.all()
    blogs=[]
    cmt = BlogComments.objects.all()
    if request.user.is_authenticated:
        blogs = UserBlogs.objects.all().order_by('-id')

    else:
        messages.error(request, 'Please login first')

    context = {
        'username': username,
        'blogs': blogs,
        'cmt': cmt,
        'user':user,
    }


    return render(request,'blogUser/Home.html',context)

@login_required()
def userProfile(request):
    username = request.session['username']
    user = loginTable.objects.get(username=request.user)
    user_User = User.objects.get(username=username)

    if request.method == "POST" :

        old_img = user.profile_picture

        if request.user.is_authenticated:
            user.first_name =request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            if request.POST['profile_picture']:

                myfile = request.POST['profile_picture']
                fs = FileSystemStorage()
                filename = fs.save(myfile)
                url = fs.url(filename)
                user.profile_picture = url
            else:
                url = old_img
                user.profile_picture = url
            user.contact_number = request.POST['contact_number']

            user_User.first_name = request.POST.get('first_name')
            user_User.last_name = request.POST.get('last_name')
            user_User.email = request.POST.get('email')

            user.save()
            user_User.save()
            messages.info(request,"Updated")
            return redirect('user_home')
        else:
            messages.info(request,"Login Again")
            return redirect('user_profile')
    else:
        messages.info(request, "POST Error")

    return render(request,'blogUser/myProfile.html',{'username':username,'user':user})


@login_required()
def addBlog(request):
    username = request.session['username']
    user = request.user
    u_blogs =UserBlogs()


    if request.user.is_authenticated:
        if request.method == 'POST':
            u_blogs.username = user
            u_blogs.title = request.POST['title']
            u_blogs.blog_image = request.FILES['blog_image']
            u_blogs.description = request.POST['description']
            u_blogs.status = 'True'

            u_blogs.save()
            return redirect('user_home')
    else:
        return redirect('addBlog')

    return render(request,'blogUser/addBlogs.html',{'username':username})


@login_required()
def BlogsActions(request):
    username = request.session['username']
    blogs = []

    if request.user.is_authenticated:
        blogs = UserBlogs.objects.filter(username=username)

    else:
        messages.error(request, 'Please login first')
    return render(request,'blogUser/BlogsActions.html',{'username':username,'blogs':blogs})


@login_required()
def EditBlog(request,blog_id):
    username = request.session['username']
    blog = UserBlogs.objects.get(id=blog_id)
    if request.user.is_authenticated:
        old_img = blog.blog_image
        if request.method == 'POST':
            blog.title = request.POST['title']
            blog.description = request.POST['description']

            if request.POST['blog_image']:

                blogfile = request.POST['blog_image']
                fs = FileSystemStorage()
                filename = fs.save(blogfile)
                url = fs.url(filename)
                blog.blog_image = url
            else:
                url = old_img
                blog.blog_image = url

            blog.save()
            messages.info(request, "Updated")
            return redirect('user_home')
    else:
        return redirect('BlogsActions')

    return render(request,'blogUser/editBlog.html',{'blog':blog,'username':username})

@login_required()
def delBlog(request,blog_id):
    blog = UserBlogs.objects.get(id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('BlogsActions')
    return render(request,'blogUser/deleteBlog.html',{'blog':blog})

@login_required()
def addComments(request,blog_id):
    blog = UserBlogs.objects.get(id=blog_id)

    b_comment = BlogComments()
    if request.user.is_authenticated:
        if request.method == 'POST':
            b_comment.username = request.user
            b_comment.title = request.POST.get('title')
            b_comment.comments = request.POST['comment']
            b_comment.save()

            return redirect('user_home')

    else:
        messages.info(request,"POST Error 😊")
        return redirect('logout')

    return render(request,'blogUser/addComments.html', {'blog': blog})

@login_required()
def blogComments(request, blog_id):
    blog = UserBlogs.objects.get(id=blog_id)
    bc = BlogComments.objects.all()
    return render(request, 'blogUser/blogComments.html', {'blog': blog,'bc':bc})
