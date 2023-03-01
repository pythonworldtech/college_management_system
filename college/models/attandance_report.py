from django.db import  models
from college.models.student import Student
from college.models.attandance import Student_Attendance



#============================ Create Student Attendance Report =============================

class Student_Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    attendance_id = models.ForeignKey(Student_Attendance, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.student_id.user.username

#===========================================================================================