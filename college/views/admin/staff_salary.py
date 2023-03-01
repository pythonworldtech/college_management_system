#================================= Import ===========================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.staff import Staff
from college.models.salary_receipt import Staff_salary_Receipt
#=======================================================================================



#=================================== Admin View Staff Salary =============================

def admin_view_staff_salary(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    action = request.GET.get('action')
                    staff_id= request.POST.get("staff_id")
                    
                    due = None
                    receipt = None
                    staff = None
                    
                    if action is not None:
                              staff = Staff.objects.filter(stf_id=staff_id)
                              
                              for st in staff:
                                        stf_id = st.id
                                        due = st.salary - st.paid_salary
                                        receipt = Staff_salary_Receipt.objects.filter(staff_id=stf_id).order_by('-created_date')
                                        
                    data = {
                              'admin':admin,
                              'salary':staff,
                              'due':due,
                              'receipt':receipt,
                              'action':action,
                              'staff_id':staff_id
                    }
                    return render(request, 'admin/view_staff_salary.html',data)
          else:
                    return redirect('login')


#==========================================================================================
#==========================================================================================




#================================= Admin View Staff Salary Receipt ==========================

def admin_view_staff_salary_receipt(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    receipt = Staff_salary_Receipt.objects.all().order_by('-created_date')
                    transaction_no= request.POST.get("transaction_no")
                    search = Staff_salary_Receipt.objects.filter(transaction_no=transaction_no).order_by('-created_date')

                    data = {
                              'admin':admin,
                              'receipt':receipt,
                              'search':search,
                              'transaction_no':transaction_no
                    }
                    return render(request, 'admin/admin_view_staff_salary_receipt.html',data)
          else:
                    return redirect('login')

#==========================================================================================



#============================= Admin Staff Salary Receipt ===================================



def admin_staff_salary_receipt(request,pk):
          if request.session.has_key('email'):
                    receipt = Staff_salary_Receipt.objects.filter(id=pk)
                    data = {
                              'receipt':receipt
                    }
                    return render(request, 'admin/salary_receipt.html',data)
          else:
                    return redirect('login')


#===========================================================================================