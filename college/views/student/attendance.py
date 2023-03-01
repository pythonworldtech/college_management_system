#======================== Import ====================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.subject import Subject
from college.models.student import Student
from college.models.session import Session
from college.models.attandance import Student_Attendance
from college.models.attandance_report import Student_Attendance_Report

#=====================================================================


#======================== View Student Attendance =====================

def student_view_attendance(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id
                    
                    student2 = Student.objects.filter(user=id)
                    for st in student2:
                              st_id = st.id
                              course = st.course_id
                    subject = Subject.objects.filter(course = course)
                    session = Session.objects.all()

                    action = request.GET.get('action')

                    get_subject = None
                    get_session = None
                    attendance_report = None

                    if action is not None:
                              if request.method=="POST":
                                        subject_id = request.POST.get("subject_id")
                                        session_id = request.POST.get("session_id")
                                        
                                        get_subject = Subject.objects.get(id=subject_id)
                                        get_session = Session.objects.get(id = session_id)
                                        attendance = Student_Attendance.objects.filter(subject_id=get_subject,session_year=get_session)
                                        
                                        for i in attendance:
                                                  id = i.id
                                                  attendance_report = Student_Attendance_Report.objects.filter(student_id=st_id,attendance_id__subject_id=subject_id)              

                    data = {
                              'admin':admin,
                              'subject':subject,
                              'session':session,
                              'action':action,
                              'get_subject':get_subject,
                              'get_session':get_session,
                              'attendance_report':attendance_report
                    }
                    
                    return render(request, 'student/student_view_attendance.html',data)
          else:
                    return redirect('login')


#=====================================================================