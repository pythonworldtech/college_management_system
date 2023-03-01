#==================================== Import ============================================

from django.shortcuts import render, redirect
from college.models.staff import Staff
from college.models.login import Login
from college.models.attandance import Staff_Attendance
#=========================================================================================



#=============================== Admin Save Staff Attendance ==============================

def admin_save_staff_attendance(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)

        
        
        staff = Staff.objects.all()
        if request.method=="POST":
            attendance_date = request.POST.get("attendance_date")
            attendance = request.POST.getlist("attendance")

            
            for i in attendance:
                stf_id = i
                int_stf = int(stf_id)
                p_staff = Staff.objects.get(id=int_stf)
                
                Staff_Attendance(
                    staff_id = p_staff,
                    attendance_date = attendance_date
                ).save()
        data = {
                'staff':staff,
                'admin':admin
        }
        return render(request, 'admin/take_staff_attendance.html',data)
    else:
        return redirect('login')
  

#===========================================================================================




#================================== Admin View Staff Attendance ============================

def admin_view_staff_attendance(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    
                    action = request.GET.get('action')
                    attendance_date = request.POST.get("attendance_date")
                    
                    attendance = None
                    
                    if action is not None:
                        if request.method=="POST":
                            attendance = Staff_Attendance.objects.filter(attendance_date=attendance_date)
                            
                    data = {
                        'admin':admin,
                        'attendance':attendance,
                        'action':action,
                        'attendance_date':attendance_date
                    }
                    return render(request, 'admin/view_staff_attendance.html',data)

          else:
              return redirect('login')

#===========================================================================================




#=============================== Admin Delete Staff Attendance =============================

def admin_delete_staff_attendance(request,pk):
    if request.session.has_key('email'):
        attendance = Staff_Attendance.objects.filter(id=pk)
        attendance.delete()
        return redirect('admin_view_staff_attendance')
    else:
        return redirect('login')
       
#============================================================================================