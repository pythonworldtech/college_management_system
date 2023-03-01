#======================== Import ====================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from college.models.fees_receipt import Student_fees_Receipt

#=====================================================================


#======================== Student Fees ================================

def student_fees(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    for a in admin:
                              id = a.id
                    
                    student2 = Student.objects.filter(user=id)
                    for st in student2:
                              student_id = st.id
                              due = st.admission_fees - st.paid_amount
                              receipt = Student_fees_Receipt.objects.filter(student_id=student_id).order_by('-created_date')

                    data = {
                              'admin':admin,
                              'fees':student2,
                              'due':due,
                              'receipt':receipt
                    }
                    return render(request, 'student/student_fees.html',data)
          else:
                    return redirect('login')


#============================================================================================
#============================================================================================




#============================= Student Fees Receipt =========================================



def student_fees_receipt(request,pk):
          if request.session.has_key('email'):
                    receipt = Student_fees_Receipt.objects.filter(id=pk)
                    data = {
                              'receipt':receipt
                    }
                    return render(request, 'student/fee_receipt.html',data)
          else:
                    return redirect('login')


#===========================================================================================