#======================== Import ====================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from college.models.staff import Staff
from college.models.student_note import Student_Note


#=====================================================================


#======================== Staff Student Fees ================================

def staff_student_notes(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    for a in admin:
                              id = a.id
                    
                    staff = Student.objects.filter(user=id)
                    get_staff = Staff.objects.get(user=id)
                    note_history = Student_Note.objects.filter(staff_id = get_staff)
                    data = {
                              'admin':admin,
                              'notes':note_history
                    }
                    return render(request, 'staff/student_notes.html',data)
          else:
                    return redirect('login')



#========================== Staff Check Student Notes =================================

def staff_student_notes_approve(request, notes_id):
    if request.session.has_key('email'):
        notes = Student_Note.objects.get(id=notes_id)
        notes.status = 1
        notes.save()
        return redirect('staff_student_notes')
    else:
        return redirect('login')

#===========================================================================================



#========================== Staff Reject Student Notes =================================

def staff_student_notes_reject(request, notes_id):
    if request.session.has_key('email'):
        notes = Student_Note.objects.get(id=notes_id)
        notes.status = 2
        notes.save()
        return redirect('staff_student_notes')
    else:
        return redirect('login')

#==========================================================================================



def staff_notes_reply(request):
    if request.session.has_key('email'):
        notes_id = request.POST.get("notes_id")
        reply = request.POST.get("reply")
        notes = Student_Note.objects.get(id=notes_id)
        notes.reply = reply
        notes.save()
        return redirect('staff_student_notes')
    else:
        return redirect('login')




