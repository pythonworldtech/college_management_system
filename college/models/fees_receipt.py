from django.db import  models
from college.models.student import Student



#================================ Create Student Fees Receipt ================================

class Student_fees_Receipt(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    transaction_no = models.CharField(max_length=100)
    paid_amount = models.IntegerField()
    payment_id = models.CharField(max_length=200)
    remark = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.transaction_no


#===========================================================================================