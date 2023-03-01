#======================== Import =======================================================

from django.shortcuts import render, redirect
from college.models.student import Student
from college.models.login import Login
from college.models.student import Student
from college.models.notification import Student_notification

#===========================================================================================


#======================== Student Notification ============================================

def student_notification(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    student = Student.objects.filter(user=id)
                    for st in student:
                              student_id = st.id

                              notification = Student_notification.objects.filter(student_id=student_id)
                    
                    data = {
                    'notification':notification,
                    'admin':admin,
                    'student':student
                    }
                    return render(request, 'student/student_notification.html',data)
          else:
                    return redirect('login')



#===========================================================================================


#======================== Student Read Notification ========================================

def student_read_notification(request,status):
          if request.session.has_key('email'):
                    notification = Student_notification.objects.get(id=status)
                    notification.status = 1
                    notification.save()
                    return redirect('student_notification')
          else:
                    return redirect('login')



#===========================================================================================