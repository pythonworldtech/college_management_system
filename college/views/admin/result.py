#==================================== Import ============================================

from django.contrib import messages
from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.subject import Subject
from college.models.student import Student
from college.models.session import Session
from college.models.result import Result
#============================================================================================



#================================ Admin Add Result ==========================================

def admin_add_result(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    
                    subject = Subject.objects.all()
                    session = Session.objects.all()
                    action = request.GET.get('action')

                    get_subject = None
                    get_session = None
                    student = None
                    
                    if action is not None:
                              if request.method=="POST":
                                        subject_id = request.POST.get("subject_id")
                                        session_id = request.POST.get("session_id")
                                        
                                        get_subject = Subject.objects.get(id=subject_id)
                                        get_session = Session.objects.get(id = session_id)
                                        
                                        subject = Subject.objects.filter(id = subject_id)
                                        
                                        for i in subject:
                                                  student_id = i.course.id
                                                  student = Student.objects.filter(course_id = student_id)
                                                  
                    data = {
                                        'subject':subject,
                                        'session':session,
                                        'action':action,
                                        'get_subject': get_subject,
                                        'get_session': get_session,
                                        'student':student,
                                        'admin':admin
                                        }
                    return render(request, 'admin/add_result.html',data)

          else:
                    return redirect('login')

#===========================================================================================



#=============================== Admin Save Student Result ==================================

def admin_save_result(request):
          if request.method=="POST":
                    subject_id = request.POST.get("subject_id")
                    session_id = request.POST.get("session_id")
                    student_id = request.POST.get("student_id")
                    internal_marks = request.POST.getlist("internal_marks")
                    external_marks = request.POST.getlist("external_marks")


                    get_subject = Subject.objects.get(id=subject_id)
                    get_session = Session.objects.get(id = session_id)
                    get_student = Student.objects.get(id = student_id)

                    check_exist = Result.objects.filter(subject_id=get_subject, student_id=get_student,session_id=get_session).exists()
                    for i in internal_marks:
                              stu_id1 = i
                              int_stu1 = int(stu_id1)

                    for j in external_marks:
                              stu_id2 = j
                              int_stu2 = int(stu_id2)
                    
                    if check_exist:
                              result = Result.objects.get(subject_id=get_subject, student_id=get_student,session_id=get_session)
                              result.internal_marks = int_stu1
                              result.external_marks = int_stu2
                              result.total_marks = int_stu1+int_stu2
                              result.save()
                              messages.success(request, "Successfully Updated Result")
                              return redirect('admin_add_result')

                    else:
                              


                              result = Result(
                                        student_id=get_student,
                                        subject_id=get_subject,
                                        session_id=get_session,
                                        internal_marks = int_stu1,
                                        external_marks = int_stu2,
                                        total_marks = int_stu1+int_stu2)
                              result.save()
                              messages.success(request, "Successfully Added Result")
                              return redirect('admin_add_result')
            
#===========================================================================================



#+================================ Admin View Student Result ================================

def admin_view_result(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    
                    subject = Subject.objects.all()
                    session = Session.objects.all()
                    action = request.GET.get('action')
                    
                    get_subject = None
                    get_session = None
                    student = None
                    total = None
                    
                    if action is not None:
                              if request.method=="POST":
                                        subject_id = request.POST.get("subject_id")
                                        session_id = request.POST.get("session_id")
                                        
                                        get_subject = Subject.objects.get(id=subject_id)
                                        get_session = Session.objects.get(id = session_id)
                                        
                                        student = Result.objects.filter(subject_id=get_subject, session_id=get_session)                 
                                        
                    data = {
                              'subject':subject,
                              'session':session,
                              'action':action,
                              'get_subject':get_subject,
                              'get_session':get_session,
                              'student':student,
                              'admin':admin,
                              'total':total
                    }
                    return render(request, 'admin/view_result.html',data)
          else:
              return redirect('login')

#=============================================================================================



#================================== Admin Edit Student Result=================================

def admin_edit_result(request,pk):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    result = Result.objects.filter(id=pk)
                    
                    if request.method=="POST":
                              internal = request.POST.get("internal_marks")
                              external = request.POST.get("external_marks")

                              internal2 = int(internal)
                              external2 = int(external)

                              student_result = Result.objects.get(id=pk)
                              student_result.internal_marks = internal
                              student_result.external_marks = external
                              student_result.total_marks = internal2 +external2
                              student_result.save()
                              messages.success(request, 'Result Updated Successfully')
                              return redirect(f"/admin_edit_result{pk}")

                    data = {
                              'admin':admin,
                              'result':result

                    }

                    return render(request, 'admin/edit_result.html',data)
          else:
                    return redirect('login')

#===========================================================================================




#====================================== Admin Delete Student Result =========================

def admin_delete_result(request,pk):
    if request.session.has_key('email'):
        result= Result.objects.filter(id=pk)
        result.delete()
        messages.warning(request, 'Result Delete Successfully')
        return redirect('admin_view_result')
    else:
        return redirect('login')

#============================================================================================