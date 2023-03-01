#================================= Import ===========================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.staff import Staff
from college.models.notification import Staff_notification
#========================================================================================


#=============================== Staff Notification =====================================

def staff_notification(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    staff = Staff.objects.filter(user=id)
                    for st in staff:
                              staff_id = st.id

                              notification = Staff_notification.objects.filter(staff_id=staff_id)
                    
                    data = {
                    'notification':notification,
                    'admin':admin,
                    'staff':staff
                    }
                    return render(request, 'staff/staff_notification.html',data)
          else:
                    return redirect('login')

#===========================================================================================
#===========================================================================================


#================================= Staff Read Notification =================================

def staff_read_notification(request,status):
          if request.session.has_key('email'):
                    notification = Staff_notification.objects.get(id=status)
                    notification.status = 1
                    notification.save()
                    return redirect('staff_notification')
          else:
                    return redirect('login')

#============================================================================================