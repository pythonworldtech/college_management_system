from django.db import  models
from college.models.student import Student
from college.models.staff import Staff




#================================ Create Student Leave ========================================

class Student_Leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.student_id.user.username

#============================================================================================



#================================ Create Staff Leave ========================================

class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.staff_id.user.username

#============================================================================================