#======================== Import ====================================

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.student import Student
from college.models.login import Login
from college.models.student import Student
from college.models.leave import Student_Leave

#=====================================================================


#======================== Student Apply Leave =========================

def student_apply_leave(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    student = Student.objects.filter(user=id)
                    for st in student:
                              student_id = st.id

                              leave = Student_Leave.objects.filter(student_id=student_id)

                    data = {
                              'admin':admin,
                              'leave':leave
                    }
                    return render(request, 'student/apply_leave.html',data)
          else:
                    return redirect('login')

#============================================================================

#======================== Student Save Leave ================================

def student_save_leave(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    student = Student.objects.get(user=id)
                    if request.method=="POST":
                              leave_date = request.POST.get("leave_date")
                              leave_message = request.POST.get("leave_message")
                              leave = Student_Leave(
                                        student_id=student,
                                        date = leave_date,
                                        message = leave_message
                              )
                              leave.save()
                              messages.success(request, "Apply For Leave Send Successfully")
                              return redirect('student_apply_leave')
          else:
                    return redirect('login')


#======================================================================================