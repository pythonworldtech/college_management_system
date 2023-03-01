#======================== Import ====================================

from college.models.login import Login
from django.shortcuts import render, redirect
from college.models.student import Student

#=====================================================================


#======================== Student Home Page =======================

def student_home(request):
          if request.session.has_key('email'):
                    user = request.session["email"]
                    customer = Login.objects.filter(email=user)
                    for c in customer:
                              id = c.id

                    student2 = Student.objects.filter(user=id)
                    for c in customer:
                              first_name=c.first_name
                              last_name=c.last_name
                              image=c.profile_pic
                              data = {
                                        'first_name':first_name,
                                        'last_name':last_name,
                                        'image':image,
                                        'admin':customer,
                                        'student':student2

                              }
                    return render(request, 'student/home.html',data)
          else:
                    return redirect('login')