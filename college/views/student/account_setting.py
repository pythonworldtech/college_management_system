#======================== Import ====================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from django.contrib import messages

#=====================================================================


#======================== Student Account Settings =======================

def student_change_email(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    user = Login.objects.filter(email=email)
                    user2 = Login.objects.get(email=email)
                    
                    for c in user:
                              id = c.id
                              student = Student.objects.filter(user=id)
                              if request.method == 'POST':
                                        email = request.POST.get("email_id")
                                        user2.email = email
                                        user2.save()
                                        return redirect('login')
                    data = {
                              'admin':user,
                              'student':student
                    }
                    return render(request, 'student/change_email.html',data)
          else:
                    return redirect('login')

#==========================================================================================





#=================================== Student Change Password ==============================

def student_change_password(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    user = Login.objects.filter(email=email)
                    user2 = Login.objects.get(email=email)
                    error_message = None
                    for c in user:
                              id = c.id
                              student = Student.objects.filter(user=id)
                              if request.method == 'POST':
                                        npassword = request.POST.get("npassword")
                                        cnpassword = request.POST.get("cnpassword")
                                        if(not npassword ):
                                                  error_message = 'Please Enter New Password'
                                        elif not cnpassword:
                                                  error_message = "Please Enter Confirm New Password !!"
                                        elif not npassword == cnpassword :
                                                  error_message = "Password & Confirm Password Should be Same !!"
                                        if not error_message:
                                                  messages.success(request, 'Password Changed Successfully')
                                                  user2.password = npassword
                                                  user2.save()
                                                  return redirect('student_change_password')
                    data = {
                              'admin':user,
                              'student':student,
                              'error':error_message
                    }
                    return render(request, 'student/change_password.html',data)
          else:
                    return redirect('login')
