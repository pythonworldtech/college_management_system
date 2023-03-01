#=================================== Import ================================================

from django.shortcuts import redirect
from college.models.login import Login
from college.models.student import Student
from college.models.fees_receipt import Student_fees_Receipt
from django.http import JsonResponse
import random
#===========================================================================================



#================================= Student Proceed To Pay ===================================

def proceed_to_pay(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    if request.method == 'POST':
                              admission_fees = request.POST.get('admission_fees')
                              fees = request.POST.get('fees')
                              paid_fees = request.POST.get('paid_fees')
                              remark = request.POST.get('remark')
                              payment_id = request.POST.get('payment_id')
                              
                              admission_fees2 = int(admission_fees)
                              fees2 = int(fees)
                              paid_fees2 = int(paid_fees)

                    for a in admin:
                              id = a.id
                              student = Student.objects.get(user=id)
                              student.paid_amount = paid_fees2 + fees2
                              student.due_amount = admission_fees2 - paid_fees2
                              student.save()


                              transaction_no = random.randint(111111111,999999999)
                              while Student_fees_Receipt.objects.filter(transaction_no = transaction_no) is None:
                                        transaction_no = random.randint(111111111,999999999)
                                        transaction_no = transaction_no

                              Student_fees_Receipt(
                                        student_id = student,
                                        transaction_no = transaction_no,
                                        paid_amount = fees,
                                        payment_id = payment_id,
                                        remark = remark

                              ).save()
                              return JsonResponse({'status':"Your Fees Paid Successfully"})
                    return redirect('student_fees')
                    
          else:
                    return redirect('login')
        
#==========================================================================================
        
