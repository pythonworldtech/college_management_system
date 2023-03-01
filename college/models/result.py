from django.db import  models
from college.models.student import Student
from college.models.subject import Subject
from college.models.session import Session



#================================ Create Result ============================================

class Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete = models.DO_NOTHING)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.student_id.user.first_name

#==========================================================================================