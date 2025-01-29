from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ResetPasswordView

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-sent/',auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Accounts/passwordReset.html'),
         name='password-reset-confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Accounts/password_reset_complete.html'),
         name='password_reset_complete')
]

