#======================== Import ====================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from college.models.staff import Staff
from college.models.student_note import Student_Note
from college.models.subject import Subject
from django.contrib import messages
#=====================================================================



#======================== Student Notes ================================

def student_notes(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    for a in admin:
                              id = a.id
                    
                    student2 = Student.objects.filter(user=id)
                    get_student = Student.objects.get(user=id)
                    for st in student2:
                              course = st.course_id
                    all_subject = Subject.objects.filter(course = course)
                    all_faculty = Staff.objects.all()
                    note_history = Student_Note.objects.filter(student_id = get_student)
                    data = {
                              'admin':admin,
                              'subject':all_subject,
                              'faculty':all_faculty,
                              'notes':note_history
                    }
                    return render(request, 'student/student_notes.html',data)
          else:
                    return redirect('login')

#===========================================================================================



#======================== Student Submit Notes ==============================================

def student_submit_notes(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    for a in admin:
                              id = a.id
                    
                    student3 = Student.objects.get(user=id)
                    if request.method=="POST":
                              topic = request.POST.get("topic")
                              subject_id = request.POST.get("subject")
                              faculty_id = request.POST.get("faculty")
                              notes = request.FILES.get("notes")
                              
                              
                                        
                              
                              subject = Subject.objects.get(id=subject_id)
                              faculty = Staff.objects.get(id=faculty_id)
                              
                              note = Student_Note(
                                        student_id = student3,
                                        staff_id = faculty,
                                        subject_id = subject,
                                        topic = topic,
                                        notes = notes
                              )
                              note.save()
                              messages.success(request, 'Notes Submit Successfully')
                              return redirect('student_notes')
          else:
                    return redirect('login')

#============================================================================================
