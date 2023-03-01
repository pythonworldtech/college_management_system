#================================= Import ===========================================

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.login import Login
from college.models.staff import Staff
from college.models.leave import Staff_Leave
#=========================================================================================


#============================ Staff Apply For Leave ======================================

def staff_apply_leave(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    staff = Staff.objects.filter(user=id)
                    for st in staff:
                              staff_id = st.id

                              leave = Staff_Leave.objects.filter(staff_id=staff_id)
                    data = {
                              'admin':admin,
                              'leave':leave
                    }
                    return render(request, 'staff/apply_leave.html',data)
          else:
                    return redirect('login')

#==========================================================================================
#==========================================================================================


#=================================== Staff Save Leave =====================================

def staff_save_leave(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    staff = Staff.objects.get(user=id)
                    if request.method=="POST":
                              leave_date = request.POST.get("leave_date")
                              leave_message = request.POST.get("leave_message")
                              leave = Staff_Leave(
                                        staff_id=staff,
                                        date = leave_date,
                                        message = leave_message
                              )
                              leave.save()
                              messages.success(request, "Apply For Leave Send Successfully")
                              return redirect('staff_apply_leave')
          else:
                    return redirect('login')


#=========================================================================================