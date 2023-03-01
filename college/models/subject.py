from django.db import  models
from college.models.course import Course
from college.models.staff import Staff



#================================ Create Subject ============================================

class Subject(models.Model):
    subject_id = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
    staff = models.ForeignKey(Staff, on_delete = models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.subject_name

#==========================================================================================