#================================= Import ===========================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from college.models.fees_receipt import Student_fees_Receipt
#=======================================================================================



#=================================== Staff View Student Fess =============================

def staff_view_student_fees(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    action = request.GET.get('action')
                    admission_no= request.POST.get("admission_no")
                    
                    due = None
                    receipt = None
                    student2 = None
                    
                    if action is not None:
                              student2 = Student.objects.filter(addmission_no=admission_no)
                              
                              for st in student2:
                                        student_id = st.id
                                        due = st.admission_fees - st.paid_amount
                                        receipt = Student_fees_Receipt.objects.filter(student_id=student_id).order_by('-created_date')
                                        
                    data = {
                              'admin':admin,
                              'fees':student2,
                              'due':due,
                              'receipt':receipt,
                              'action':action,
                              'admission_no':admission_no
                    }
                    return render(request, 'staff/view_student_fees.html',data)
          else:
                    return redirect('login')


#==========================================================================================
#==========================================================================================




#================================= Staff View Student Fees Receipt ==========================

def staff_view_student_fees_receipt(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    receipt = Student_fees_Receipt.objects.all().order_by('-created_date')
                    transaction_no= request.POST.get("transaction_no")
                    search = Student_fees_Receipt.objects.filter(transaction_no=transaction_no).order_by('-created_date')

                    data = {
                              'admin':admin,
                              'receipt':receipt,
                              'search':search,
                              'transaction_no':transaction_no
                    }
                    return render(request, 'staff/staff_view_student_fees_receipt.html',data)
          else:
                    return redirect('login')

#==========================================================================================



#============================= Staff Student Fees Receipt ==================================



def staff_student_fees_receipt(request,pk):
          if request.session.has_key('email'):
                    receipt = Student_fees_Receipt.objects.filter(id=pk)
                    data = {
                              'receipt':receipt
                    }
                    return render(request, 'staff/fee_receipt.html',data)
          else:
                    return redirect('login')


#===========================================================================================