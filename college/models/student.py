from django.db import  models
from college.models.course import Course
from college.models.session import Session
from college.models.login import Login



#================================ Create Student ============================================

class Student(models.Model):
          user = models.ForeignKey(Login, on_delete = models.CASCADE)
          addmission_no = models.CharField(max_length=50)
          gender = models.CharField(max_length=50)
          course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
          session_year_id = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
          address = models.CharField(max_length=50)
          mobile = models.CharField(max_length=50)
          dob = models.CharField(max_length=50)
          father_name = models.CharField(max_length=50)
          mother_name = models.CharField(max_length=50)
          parent_mobile_no = models.CharField(max_length=50)
          admission_fees = models.IntegerField(default=0)
          paid_amount = models.IntegerField(default=0)
          created_date = models.DateTimeField(auto_now_add=True)
          
          
          def __self__(self):
                    return self.user.username


          def register(self):
                    self.save()

#=========================================================================================