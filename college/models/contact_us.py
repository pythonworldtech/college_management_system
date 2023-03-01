from django.db import  models


#================================ Create Contact ============================================

class Contact_Us(models.Model):
    reference_no = models.CharField(max_length=255,unique=True)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.reference_no

#==========================================================================================