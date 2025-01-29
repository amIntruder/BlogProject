from django.db import models

from Accountsapp.models import loginTable
from django.contrib.auth.models import User


# Create your models here.

class UserBlogs(models.Model):
    title = models.CharField(max_length=200,null=True)
    blog_image = models.ImageField(upload_to='blog_media', null=True)
    description = models.TextField(max_length=10000, null=True)
    username = models.CharField(max_length=200, null=True)
    status = models.CharField(default='True',max_length=100,null=True)

    def __str__(self):
        return '{}'.format(self.title)


class BlogComments(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    comments = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return '{}'.format(self.title)