#================================= Import ===========================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.staff import Staff
from college.models.salary_receipt import Staff_salary_Receipt
#=======================================================================================




#================================= Staff View Salary Receipt ==========================

def staff_view_staff_salary_receipt(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    for a in admin:
                              id = a.id
                    
                    staff = Staff.objects.filter(user=id)
                    for st in staff:
                              staff_id = st.id
                    receipt = Staff_salary_Receipt.objects.filter(staff_id=staff_id)
                    transaction_no= request.POST.get("transaction_no")
                    search = Staff_salary_Receipt.objects.filter(staff_id=staff_id,transaction_no=transaction_no)

                    data = {
                              'admin':admin,
                              'receipt':receipt,
                              'search':search,
                              'transaction_no':transaction_no
                    }
                    return render(request, 'staff/view_staff_salary_receipt.html',data)
          else:
                    return redirect('login')

#==========================================================================================


#============================= Staff Salary Receipt =========================================



def staff_salary_receipt(request,pk):
          if request.session.has_key('email'):
                    receipt = Staff_salary_Receipt.objects.filter(id=pk).order_by('-created_date')
                    data = {
                              'receipt':receipt
                    }
                    return render(request, 'staff/salary_receipt.html',data)
          else:
                    return redirect('login')


#===========================================================================================