from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . models import loginTable
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_exist = User.objects.filter(username=username, password=password).exists()
        try:

            if user_exist is not None:

                user_details = loginTable.objects.get(username=username)
                if user_details.status == 'True':
                    user_p = loginTable.objects.get(username=username)
                    user_p.password = user_details.password
                    user_p.save()
                    type = user_p.type
                    if type == 'user':
                        user = authenticate(username=username, password=password)
                        request.session['username'] = username
                        login(request, user)
                        messages.success(request, "User Successfully Logged In")
                        return redirect('user_home')
                    elif type == 'admin':
                        user = authenticate(username=username, password=password)
                        request.session['username'] = username
                        login(request, user)
                        messages.success(request, "Admin Successfully Logged In")
                        return redirect('admin_home')
                    else:
                        messages.error(request,"Admin Blocked User, Please Contact Admin...")
                        return redirect('signin')
                else:
                    messages.error(request,"User is blocked by Admin")
            else:
                messages.error(request,"Register user first..")
        except:
            messages.error(request,"Invalid User Name or Password!..")
    return render(request,'Accounts/Signin.html')


def logout_view(request):
    logout(request)
    return redirect('signin')

def signup(request):

    if request.method == 'POST' and request.FILES['profile_picture']:


        myfile = request.FILES['profile_picture']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)

        login_table = loginTable(
            username = request.POST['username'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            profile_picture = url,
            contact_number = request.POST['contact_number'],
            password = request.POST['password'],
            type = 'user'
        )


        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        active = True

        if request.POST.get('password') == request.POST.get('c_password'):
            login_table.save()

            user = User.objects.create(
                username= username,
                first_name =first_name,
                last_name =last_name,
                email =email,
                is_active = active,
            )
            user.set_password(password)

            user.save()
            messages.info(request, 'Registration Success')
            return redirect('signin')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')

    return render(request,'Accounts/Signup.html')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'Accounts/password_reset.html'
    email_template_name = 'Accounts/password_reset_email.html'
    subject_template_name = 'Accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('signin')

