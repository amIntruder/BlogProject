from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from Accountsapp.models import loginTable
from Userapp.models import BlogComments, UserBlogs
from django.contrib.auth.models import User



# Create your views here.

def adminHome(request):
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
        'user': user,
    }
    return render(request,'blogAdmin/adminHome.html',context)

def blogUsers(request):
    username = request.session['username']
    users = loginTable.objects.filter(type='user')
    paginator = Paginator(users, 4)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)
    return render(request, 'blogAdmin/Blog_users.html',{'page':page,'users':users,'username':username})


@login_required()
def adminProfile(request):
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
            return redirect('admin_home')
        else:
            messages.info(request,"Login Again")
            return redirect('admin_profile')
    else:
        messages.info(request, "POST Error")

    return render(request,'blogAdmin/adminProfile.html',{'username':username,'user':user})



def viewUserBlogs(request,user_name):
    username = request.session['username']

    users = User.objects.get(username=user_name)
    blogs=[]

    u_name = users.username
    if request.user.is_authenticated:
        blogs = UserBlogs.objects.filter(username = users.username)

    else:
        messages.error(request, 'Please login first')
    return render(request, 'blogAdmin/userBlogs.html', {'username': username, 'blogs': blogs,'users':users,'u_name':u_name})


@login_required
def BlockUser(request,user_name):
    user = loginTable.objects.get(username=user_name)
    message = "Your account is blocked by Admin,"\
               "Contact Admin."
    subject = "Your Account Blocked"
    if request.user.is_authenticated:
        if request.method == 'POST':
            if user.status == 'True':
                user.status = 'False'
                user.save()
                send_mail(subject,message,settings.EMAIL_HOST_USER,[user.email])
                return redirect('blogUsers')
            else:
                messages.error(request, 'Please login first....')

    else:
        messages.error(request, 'Please login first')
    return render(request,'blogAdmin/blockUser.html',{'user':user})

def unBlockUser(request,user_name):
    user = loginTable.objects.get(username=user_name)

    message = "Your account is un_blocked by Admin,"\
               "Continue your journey with My Blog."
    subject = "Your Account un_Blocked"


    if request.user.is_authenticated:
        if request.method == 'POST':
            if user.status == 'False':
                user.status = 'True'
                user.save()

                send_mail(subject,message,settings.EMAIL_HOST_USER,[user.email])
                return redirect('blogUsers')
            else:
                messages.error(request, 'Please login first....')

    else:
        messages.error(request, 'Please login first')
    return render(request,'blogAdmin/unblockUser.html',{'user':user})

def blockBlogs(request,blog_id):
    blog = UserBlogs.objects.get(id = blog_id)
    name = blog.username
    user = loginTable.objects.get(username=name)

    message = "Your Blog  is blocked by Admin,"\
               "Contact Admin."
    subject = "Your Blog Blocked"
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog.status = 'False'
            blog.save()

            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
            return redirect('blogUsers')

    return render(request,'blogAdmin/blockBlog.html',{'blog':blog})


def unblockBlogs(request,blog_id):
    blog = UserBlogs.objects.get(id = blog_id)
    name = blog.username
    user = loginTable.objects.get(username=name)

    message = "Your Blog  is blocked by Admin," \
              "Contact Admin."
    subject = "Your Blog Blocked"

    if request.user.is_authenticated:
        if request.method == 'POST':
            blog.status = 'True'
            blog.save()


            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

            return redirect('blogUsers')

    return render(request,'blogAdmin/unblockBlogs.html',{'blog':blog})

def delBlog(request,blog_id):
    blog = UserBlogs.objects.get(id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogUsers')
    return render(request,'blogAdmin/delBlog.html',{'blog':blog})



def deleteUser(request,user_name):
    user = loginTable.objects.get(username=user_name)
    auth_user = User.objects.get(username=user_name)
    blog_user = UserBlogs.objects.get(username=user_name)
    if request.method == 'POST':
        if user.username == auth_user.username == blog_user.username :
            user.delete()
            auth_user.delete()
            blog_user.delete()
            return redirect('blogUsers')
        else:
            messages.error(request,"User Error")

    return render(request,'blogAdmin/deleteUser.html',{'user':user})
