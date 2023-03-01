from django.db import  models
from college.models.student import Student
from college.models.staff import Staff
from college.models.subject import Subject
import os




#================================ Create Student Notes========================================

def file_path(instance,filename):
    path = "documents/"
    format = filename
    return os.path.join(path,format)


class Student_Note(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    staff_id = models.ForeignKey(Staff, on_delete = models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)
    topic = models.CharField(max_length=50)
    notes = models.FileField(upload_to='image/download/uploads/notes/')
    status = models.IntegerField(default=0)
    reply = models.TextField(default='No Reply')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.student_id.user.username

#==========================================================================================