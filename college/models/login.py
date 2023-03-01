from django.db import  models
from django.forms import DateField




#================================ Create Login ============================================

USER = (
                    ('1','ADMIN'),
                    ('2','STAFF'),
                    ('3','STUDENT')
          )

          
class Login(models.Model):
          username = models.CharField(max_length=15,unique=True)
          first_name = models.CharField(max_length=50)
          last_name = models.CharField(max_length=50)
          email = models.CharField(max_length=100)
          user_type = models.CharField(choices=USER,max_length=50,default=1)
          profile_pic = models.ImageField(upload_to='image/download/uploads/login/')
          password = models.CharField(max_length=15)
          otp = models.CharField(max_length=15)
          created_date = models.DateTimeField(auto_now_add=True)

          def register(self):
                    self.save()
                    
          @staticmethod
          def get_customer_by_email(email):
                    try:
                              return Login.objects.get(email=email)
                    except:
                              return False
                              
                              
          def isExists(self):
                    if Login.objects.filter(username = self.username):
                              return True
                    return False
                              
          def __str__(self):
                    return self.username

#=========================================================================================
