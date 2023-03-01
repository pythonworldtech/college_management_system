#==================================== Import ============================================

from django.shortcuts import render, redirect
from college.models.leave import Staff_Leave
from college.models.login import Login
from college.models.leave import Student_Leave
from college.models.leave import Staff_Leave
#==========================================================================================


#=================================== Admin View Staff Leave ===============================

def admin_view_staff_leave(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    staff_leave = Staff_Leave.objects.all()

                    data = {
                              'admin':admin,
                              'staff_leave':staff_leave
                    }
                    return render(request, 'admin/view_staff_leave.html',data)
          else:
              return redirect('login')



#========================== Admin Approved Staff Leave ====================================

def admin_staff_leave_approve(request, leave_id):
    if request.session.has_key('email'):
        leave = Staff_Leave.objects.get(id=leave_id)
        leave.status = 1
        leave.save()
        return redirect('admin_view_staff_leave')
    else:
        return redirect('login')

#============================================================================================



#=========================== Admin Rejected Staff Leave =====================================

def admin_staff_leave_reject(request, leave_id):
    if request.session.has_key('email'):
        leave = Staff_Leave.objects.get(id=leave_id)
        leave.status = 2
        leave.save()
        return redirect('admin_view_staff_leave')
    else:
        return redirect('login')

#============================================================================================


#============================ Admin View Student Leave =====================================

def admin_view_student_leave(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    student_leave = Student_Leave.objects.all()

                    data = {
                              'admin':admin,
                              'student_leave':student_leave
                    }

                    return render(request, 'admin/view_student_leave.html',data)
          else:
              return redirect('login')

#========================================================================================



#========================== Admin Approved Student Leave =================================

def admin_student_leave_approve(request, leave_id):
    if request.session.has_key('email'):
        leave = Student_Leave.objects.get(id=leave_id)
        leave.status = 1
        leave.save()
        return redirect('admin_view_student_leave')
    else:
        return redirect('login')

#===========================================================================================



#========================== Admin Rejected Student Leave ====================================

def admin_student_leave_reject(request, leave_id):
    if request.session.has_key('email'):
        leave = Student_Leave.objects.get(id=leave_id)
        leave.status = 2
        leave.save()
        return redirect('admin_view_student_leave')
    else:
        return redirect('login')

#==========================================================================================