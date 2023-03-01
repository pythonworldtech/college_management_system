from django.db import  models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
          USER = (
                    ('1','ADMIN'),
                    ('2','STAFF'),
                    ('3','STUDENT')
          )

          user_type = models.CharField(choices=USER,max_length=50,default=1)
          profile_pic = models.ImageField(upload_to='image/download/uploads/profile_pic/')
          mobile_number = models.CharField(max_length=50,default='',null=True,blank=True)
          address = models.CharField(max_length=50,default='',null=True,blank=True)
          dob = models.CharField(max_length=10,null=True,blank=True)



