from django.db import  models


#================================ Create Session ============================================

class Session(models.Model):
    session_start = models.CharField(max_length=255)
    session_end = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.session_start + " " + self.session_end

#===========================================================================================