#==================================== Import ============================================

from django.contrib import messages
from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.course import Course
from college.models.staff import Staff
from college.models.subject import Subject
import random
#==========================================================================================



#================================ Admin Add Subject ========================================

def admin_add_subject(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    course_name = Course.objects.all()
                    staff_name = Staff.objects.all()

                    
                    subject = ['SUB']
                    subject_id =f'{random.choice(subject)}-0{random.randint(100,999)}'
                    while Subject.objects.filter(subject_id = subject_id) is None:
                              subject_id =f'{random.choice(course)}-0{random.randint(100,999)}'
                              subject_id = subject_id
                              
                    if request.method=="POST":
                              subject_id = request.POST.get("subject_id")
                              subject_name = request.POST.get("subject_name")
                              course = request.POST.get("course")
                              staff = request.POST.get("staff")
                              print(course,staff)

                              course_id = Course.objects.get(id=course)
                              staff_id = Staff.objects.get(id=staff)
                              
                              subject = Subject(
                                        subject_id = subject_id,
                                        subject_name = subject_name,
                                        course = course_id,
                                        staff = staff_id
                              )
                              subject.save()
                              messages.success(request, 'Subject Added Successfully')
                              return redirect('admin_add_subject')
                    else:
                              for c in admin:
                                        ftname=c.first_name
                                        ltname=c.last_name
                                        image=c.profile_pic
                                        
                              data = {
                                        'first_name':ftname,
                                        'last_name':ltname,
                                        'image':image,
                                        'admin':admin,
                                        'subject_id':subject_id,
                                        'course':course_name,
                                        'staff':staff_name
                              }
                              return render(request, 'admin/add_subject.html',data)
          else:
                    return redirect('login')

#===========================================================================================




#================================= Admin Manage Subject =====================================

def admin_manage_subject(request):
  if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        subject = Subject.objects.all().order_by('-created_date')
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'subject':subject,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
          }
        return render(request, 'admin/manage_subject.html',data)
  else:
    return redirect('login')

#===========================================================================================




#=================================== Admin Edit Subject =====================================

def admin_edit_subject(request,pk):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        subject = Subject.objects.filter(id=pk)
        course_name = Course.objects.all()
        staff_name = Staff.objects.all()

        for c in subject:
                  id = c.id
                    
        error_message = None
                    
        if request.method=="POST":
            subject_name = request.POST['subject_name']
            course = request.POST['course']
            staff = request.POST['staff']

            course_id = Course.objects.get(id=course)
            staff_id = Staff.objects.get(id=staff)
            
            update_subject = Subject.objects.get(id=id)
            update_subject.subject_name = subject_name
            update_subject.course = course_id
            update_subject.staff = staff_id
            update_subject.save()
            messages.success(request, 'Subject Updated Successfully')
            return redirect(f"/admin_edit_subject{pk}")
                              
        else:
            
            for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic

            data = {
                'first_name':ftname,
                'last_name':ltname,
                'image':image,
                'admin':admin,
                'error':error_message,
                'subject':subject,
                'course':course_name,
                'staff':staff_name
                }
            return render(request, 'admin/edit_subject.html',data)
    else:
        return redirect('login')

#===========================================================================================



#================================= Admin Delete Subject =====================================

def admin_delete_subject(request,pk):
    if request.session.has_key('email'):
        subject = Subject.objects.filter(id=pk)
        subject.delete()
        messages.warning(request, 'Subject Delete Successfully')
        return redirect('admin_manage_subject')
    else:
        return redirect('login')

#==========================================================================================