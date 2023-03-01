from django.db import  models


#================================ Create Course =============================================

class Course(models.Model):
    course_id = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    course_pic = models.ImageField(upload_to='image/download/uploads/course/')
    course_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.course_name

#===========================================================================================