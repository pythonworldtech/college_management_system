#==================================== Import ============================================

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.student import Student
from college.models.login import Login
from college.models.staff import Staff
from college.models.notification import Staff_notification
from college.models.notification import Student_notification
#==========================================================================================



#=============================== Admin Send Staff Notification ============================

def admin_send_staff_notification(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    staff = Staff.objects.all()
                    notification = Staff_notification.objects.all()
                    
                    data = {
                              'staff':staff,
                              'admin':admin,
                              'notification':notification
                    }
                    return render(request, 'admin/send_staff_notification.html',data)
          else:
                    return redirect('login')

#==========================================================================================



#============================ Admin Save Staff Notification ===============================

def admin_save_staff_notification(request):
          if request.session.has_key('email'):
                    if request.method=="POST":
                              email = request.session["email"]
                              admin = Login.objects.filter(email=email)
                              staff = Staff.objects.all()
                              notification = Staff_notification.objects.all()
                              
                              staff_id = request.POST.get("staff_id")
                              message = request.POST.get("message")
                              
                              send_staff = Staff.objects.get(user=staff_id)
                              
                              notification = Staff_notification(
                                        staff_id = send_staff,
                                        message = message
                              )
                              notification.save()
                              messages.success(request,'Staff Notification Send Successfully')
                              return redirect('admin_send_staff_notification')
                    data = {
                              'admin':admin,
                              'staff':staff,
                              'notification':notification
                    }
                    return render(request, 'admin/send_staff_notification.html',data)
          else:
                    return redirect('login')


#========================================================================================




#============================ Admin Send Student Notification ============================

def admin_send_student_notification(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    student = Student.objects.all()
                    notification = Student_notification.objects.all()
                    
                    data = {
                              'student':student,
                              'admin':admin,
                              'notification':notification
                    }
                    return render(request, 'admin/send_student_notification.html',data)
          else:
                    return redirect('login')

#========================================================================================



#============================== Admin Save Student Notification ==========================

def admin_save_student_notification(request):
          if request.session.has_key('email'):
                    if request.method=="POST":
                              student_id = request.POST.get("student_id")
                              message = request.POST.get("message")

                              email = request.session["email"]
                              admin = Login.objects.filter(email=email)
                              staff = Staff.objects.all()
                              notification = Staff_notification.objects.all()
                              
                              send_student = Student.objects.get(user=student_id)
                              
                              notification = Student_notification(
                                        student_id = send_student,
                                        message = message
                              )
                              notification.save()
                              messages.success(request,'Student Notification Send Successfully')
                              return redirect('admin_send_student_notification')

                    data = {
                              'admin':admin,
                              'staff':staff,
                              'notification':notification
                    }
                    return render(request, 'admin/send_student_notification.html',data)
          else:
                    return redirect('login')


#===========================================================================================