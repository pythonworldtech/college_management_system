#================================= Import ===========================================

from django.shortcuts import render, redirect
from college.models.student import Student
from college.models.staff import Staff
from college.models.login import Login
from college.models.session import Session
from college.models.subject import Subject
from college.models.attandance import Student_Attendance
from college.models.attandance import Staff_Attendance
from college.models.attandance_report import Student_Attendance_Report

#==========================================================================================

#================================= Take Student Attendance ================================

def staff_take_attendance(request):
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
                                        
                                        subject = Subject.objects.filter(id=subject_id)
                                        
                                        for i in subject:
                                                  student_id = i.course.id
                                                  student = Student.objects.filter(course_id=student_id)
                                                  
                    data = {
                              'subject':subject,
                              'session':session,
                              'action':action,
                              'get_subject': get_subject,
                              'get_session': get_session,
                              'student':student,
                              'admin':admin
                    }
                    return render(request, 'staff/take_student_attendance.html',data)
          else:
                    return redirect('login')

#===========================================================================================
#===========================================================================================

#+=========================== Save Student Attendance ======================================

def staff_save_student_attendance(request):
          if request.session.has_key('email'):

                    if request.method=="POST":
                              subject_id = request.POST.get("subject_id")
                              session_id = request.POST.get("session_id")
                              attendance_date = request.POST.get("attendance_date")
                              student_id = request.POST.getlist("attendance")
                              
                              get_subject = Subject.objects.get(id=subject_id)
                              get_session = Session.objects.get(id = session_id)
                              
                              save_attendance = Student_Attendance(
                                        subject_id = get_subject,
                                        session_year = get_session,
                                        attendance_date = attendance_date
                              )
                              save_attendance.save()
                              
                              for i in student_id:
                                        stu_id = i
                                        int_stu = int(stu_id)
                                        p_student = Student.objects.get(id=int_stu)
                                        
                                        Student_Attendance_Report(
                                                  student_id = p_student,
                                                  attendance_id = save_attendance
                                        ).save()
                    return redirect('staff_take_attendance')

          else:
                    return redirect('login')
          
          
#===========================================================================================
#===========================================================================================



#=============================== View Student Attendance ====================================

def staff_view_student_attendance(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    
                    subject = Subject.objects.all()
                    session = Session.objects.all()
                    action = request.GET.get('action')
                    attendance_date = request.POST.get("attendance_date")
                    
                    get_subject = None
                    get_session = None
                    attendance_report = None
                    attendance = None
                    
                    if action is not None:
                              if request.method=="POST":
                                        subject_id = request.POST.get("subject_id")
                                        session_id = request.POST.get("session_id")
                                        
                                        get_subject = Subject.objects.get(id=subject_id)
                                        get_session = Session.objects.get(id = session_id)
                                        
                                        attendance = Student_Attendance.objects.filter(subject_id=get_subject, attendance_date=attendance_date,session_year=get_session)
                                        
                                        for i in attendance:
                                                  id = i.id
                                                  attendance_report = Student_Attendance_Report.objects.filter(attendance_id=id)
                                                  
                    data = {
                              'subject':subject,
                              'session':session,
                              'action':action,
                              'get_subject':get_subject,
                              'get_session':get_session,
                              'attendance_date':attendance_date,
                              'attendance_report':attendance_report,
                              'attendance':attendance,
                              'admin':admin
                    }
                    return render(request, 'staff/view_student_attendance.html',data)
          else:
                    return redirect('login')

#===========================================================================================
#===========================================================================================



#==================================== View Attandance ======================================

def staff_view_attendance(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    staff = Staff.objects.filter(user=id)
                    for stf in staff:
                              stf_id = stf.id
                              attendance = Staff_Attendance.objects.filter(staff_id=stf_id)
                              
                    data = {
                              'admin':admin,
                              'attendance':attendance,
                    }
                    return render(request, 'staff/view_staff_attendance.html',data)
          else:
                    return redirect('login')

#============================================================================================
#============================================================================================