#==================================== Import ============================================

from college.models.course import Course
from college.models.login import Login
from django.shortcuts import render, redirect
from college.models.student import Student
from college.models.course import Course
from college.models.staff import Staff
from college.models.subject import Subject
#===========================================================================================


#================================= Admin Home Page =========================================

def admin_home(request):
          if request.session.has_key('email'):
                    user = request.session["email"]
                    customer = Login.objects.filter(email=user)
                    student=Student.objects.all().count()
                    staff=Staff.objects.all().count()
                    course=Course.objects.all().count()
                    subject=Subject.objects.all().count()
                    for c in customer:
                              first_name=c.first_name
                              last_name=c.last_name
                              image=c.profile_pic
                              data = {
                                        'first_name':first_name,
                                        'last_name':last_name,
                                        'image':image,
                                        'admin':customer,
                                        'student':student,
                                        'staff':staff,
                                        'course':course,
                                        'subject':subject

                              }
                    return render(request, 'admin/home.html',data)
          else:
                    return redirect('login')

#==========================================================================================