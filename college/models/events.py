from django.db import  models


#================================ Create Event ============================================

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField(auto_now_add=True)
    event_place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/download/uploads/events/')
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

#==========================================================================================