from django.db import  models
from college.models.staff import Staff



#=============================== Create Staff Salary Receipt ================================

class Staff_salary_Receipt(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.DO_NOTHING)
    transaction_no = models.CharField(max_length=100)
    salary_paid = models.IntegerField()
    payment_id = models.CharField(max_length=200)
    remark = models.TextField(default='')
    account_no = models.CharField(max_length=50,default='')
    ifsc_code = models.CharField(max_length=50,default='')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                    return self.transaction_no

#=========================================================================================