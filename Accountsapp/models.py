from django.db import models
# Create your models here.

class loginTable(models.Model):
    username = models.CharField(max_length=200, null=True,unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True,unique=True)
    profile_picture =models.URLField(max_length=200, null=True)
    contact_number = models.IntegerField(null=True)
    status = models.CharField(default='True',max_length=100,null=True)
    password = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.username)

