from django.db import  models
from college.models.course import Course


#==================================== Create Admission Model ==============================

class Admission(models.Model):
    application_no = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.application_no

#==========================================================================================