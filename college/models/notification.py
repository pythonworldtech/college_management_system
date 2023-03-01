from django.db import  models
from college.models.student import Student
from college.models.staff import Staff



#================================ Create Staff Notification ==================================

class Staff_notification(models.Model):
          staff_id = models.ForeignKey(Staff, on_delete = models.DO_NOTHING)
          message = models.TextField()
          status = models.IntegerField(null=True,default=0)
          created_date = models.DateTimeField(auto_now_add=True)

          def __str__(self):
                    return self.staff_id.user.username

#===========================================================================================



#================================ Create Student Notification ===============================

class Student_notification(models.Model):
          student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
          message = models.TextField()
          status = models.IntegerField(null=True,default=0)
          created_date = models.DateTimeField(auto_now_add=True)

          def __str__(self):
                    return self.student_id.user.username

#============================================================================================