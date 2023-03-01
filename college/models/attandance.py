from django.db import  models
from college.models.subject import Subject
from college.models.session import Session
from college.models.staff import Staff



#================================ Create Student Attendance ==============================

class Student_Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)
    session_year = models.ForeignKey(Session, on_delete = models.DO_NOTHING)
    attendance_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.subject_id.subject_name

#===========================================================================================




#================================ Create Staff Attendance ==============================

class Staff_Attendance(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.DO_NOTHING)
    attendance_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.staff_id.user.username

#==========================================================================================