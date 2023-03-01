from django.db import  models


#================================ Create Gallery ============================================

class Gallery(models.Model):
    gallery_name = models.CharField(max_length=255)
    gallery_pic = models.ImageField(upload_to='image/download/uploads/gallery/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.gallery_name

#===========================================================================================