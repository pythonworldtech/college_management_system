#==================================== Import ============================================

from django.contrib import messages
from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.course import Course
import random
#==========================================================================================


#================================== Admin Add Course =======================================

def admin_add_course(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    
                    course = ['COURSE']
                    course_id =f'{random.choice(course)}-0{random.randint(100,999)}'
                    while Course.objects.filter(course_id = course_id) is None:
                              course_id =f'{random.choice(course)}-0{random.randint(100,999)}'
                              course_id = course_id
                              
                    if request.method=="POST":
                              course_id = request.POST.get("course_id")
                              course_name = request.POST.get("course_name")
                              course_image = request.FILES.get("course_pic")
                              course_description = request.POST.get("course_desc")
                              
                              course = Course(
                                        course_id = course_id,
                                        course_name = course_name,
                                        course_pic = course_image,
                                        course_description = course_description
                              )
                              course.save()
                              messages.success(request, 'Course Added Successfully')
                              return redirect('admin_add_course')
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
                                        'course_id':course_id
                              }
                              return render(request, 'admin/add_course.html',data)
          else:
                    return redirect('login')

#==========================================================================================



#================================= Admin Manage Course =====================================

def admin_manage_course(request):
  if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        course = Course.objects.all().order_by('-created_date')
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'course':course,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
          }
        return render(request, 'admin/manage_course.html',data)
  else:
    return redirect('login')

#===========================================================================================



#===================================== Admin Edit Course ===================================

def admin_edit_course(request,pk):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        course = Course.objects.filter(id=pk)

        for c in course:
                  id = c.id
                    
        error_message = None
                    
        if request.method=="POST":
            course_name = request.POST['course_name']
            course_picture = request.FILES.get("course_pic")
            course_description = request.POST.get("course_desc")
            
            update_course = Course.objects.get(id=id)
            update_course.course_name = course_name
            #update_course.course_pic =course_picture, 
            update_course.course_description = course_description
            update_course.save()
            messages.success(request, 'Course Updated Successfully')
            return redirect(f"/admin_edit_course{pk}")
                              
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
                'course':course
                }
            return render(request, 'admin/edit_course.html',data)
    else:
        return redirect('login')

#===========================================================================================


#================================== Admin Delete Course ====================================

def admin_delete_course(request,pk):
    if request.session.has_key('email'):
        course = Course.objects.filter(id=pk)
        course.delete()
        messages.warning(request, 'Course Delete Successfully')
        return redirect('admin_manage_course')
    else:
        return redirect('login')

#============================================================================================