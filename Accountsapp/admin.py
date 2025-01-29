from django.contrib import admin

# Register your models here.

from .models import loginTable
from Userapp.models import UserBlogs,BlogComments
admin.site.register(loginTable)
admin.site.register(UserBlogs)
admin.site.register(BlogComments)
