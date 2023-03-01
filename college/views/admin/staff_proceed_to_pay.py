#===================================== Import ===============================================

from django.shortcuts import redirect
from college.models.staff import Staff
from college.models.salary_receipt import Staff_salary_Receipt
from django.http import JsonResponse
import random
#============================================================================================



#============================= Admin Staff Proceed For Payment===============================

def admin_proceed_to_pay2(request):
          if request.session.has_key('email'):
                    if request.method == 'POST':
                              stf_id = request.POST.get('stf_id')
                              salary = request.POST.get('salary')
                              salary_to_paid = request.POST.get('salary_to_paid')
                              paid_salary = request.POST.get('paid_salary')
                              remark = request.POST.get('remark')
                              payment_id = request.POST.get('payment_id')
                              account_no = request.POST.get('account_no')
                              ifsc = request.POST.get('ifsc')
                              
                              salary = int(salary)
                              salary_to_paid = int(salary_to_paid)
                              paid_salary = int(paid_salary)

                              staff = Staff.objects.get(id=stf_id)
                              staff.paid_salary = paid_salary + salary_to_paid
                              staff.due_salary = salary - paid_salary
                              staff.save()


                              transaction_no = random.randint(111111111,999999999)
                              while Staff_salary_Receipt.objects.filter(transaction_no = transaction_no) is None:
                                        transaction_no = random.randint(111111111,999999999)
                                        transaction_no = transaction_no

                              Staff_salary_Receipt(
                                        staff_id = staff,
                                        transaction_no = transaction_no,
                                        salary_paid = salary_to_paid,
                                        payment_id = payment_id,
                                        remark = remark,
                                        account_no = account_no,
                                        ifsc_code = ifsc
                              ).save()
                              return JsonResponse({'status':"Your Salary Paid Successfully"})
                    return redirect('admin_view_staff_salary')
                    
          else:
                    return redirect('login')
        
#===========================================================================================
#===========================================================================================     
