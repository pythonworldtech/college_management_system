from django.db import  models
from college.models.login import Login



#================================ Create Staff ============================================

class Staff(models.Model):
          stf_id = models.CharField(max_length=50)
          user = models.ForeignKey(Login, on_delete = models.CASCADE)
          address = models.CharField(max_length=50)
          gender = models.CharField(max_length=50)
          dob = models.CharField(max_length=50)
          mobile_number = models.CharField(max_length=50)
          salary = models.IntegerField(default=0)
          paid_salary = models.IntegerField(default=0)
          account_no = models.CharField(max_length=50,default='')
          ifsc_code = models.CharField(max_length=50,default='')
          created_date = models.DateTimeField(auto_now_add=True)
          
          
          def __self__(self):
                    return self.stf_id

          def register(self):
                    self.save()


#==========================================================================================