#================================= Import ===========================================

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.student import Student
from college.models.login import Login
from college.models.course import Course
from college.models.session import Session
import random
#=======================================================================================



#================================== Staff Add Student Result =============================

def staff_add_student(request):
          if request.session.has_key('email'):
                    error_message = None

                    
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    course = Course.objects.all()
                    session = Session.objects.all()


                    #postData = request.POST

                    if request.method=="POST":
                              first_name = request.POST.get("first_name")
                              last_name = request.POST.get("last_name")
                              addmission_no = request.POST.get("addmission_no")
                              gender = request.POST.get("gender")
                              dob = request.POST.get("dob")
                              username = request.POST.get("username")
                              address = request.POST.get("address")
                              email = request.POST.get("email")
                              mobile = request.POST.get("mobile_no")
                              image = request.FILES.get("pic")
                              father_name = request.POST.get("father_name")
                              mother_name = request.POST.get("mother_name")
                              parent_no = request.POST.get("parent_no")
                              password = request.POST.get("password")
                              course_id = request.POST.get('course_id')
                              session_id = request.POST.get('session_id')
                              admission_fees = request.POST.get('admission_fees')
                              admission_fees2= int(admission_fees)

                              #course_obj = Courses.objects.get(id=course_id)
                              courses = Course.objects.get(id=course_id)
                              session_year = Session.objects.get(id=session_id)
                              
                              
                              if Login.objects.filter(username=username).exists():
                                        messages.warning(request, 'Username Already Exists')
                                        return redirect('staff_add_student')

                              if(not first_name ):
                                        messages.warning(request, 'First Name is Required')
                                        return redirect('staff_add_student')

                              elif len(mobile) < 10:
                                        messages.warning(request, 'Mobile Number must be 10 Character long')
                                        return redirect('staff_add_student')

                              elif not last_name:
                                        messages.warning(request, 'Last Name is Required')
                                        return redirect('staff_add_student')

                              elif not email:
                                        messages.warning(request, 'Email Id is Required')
                                        return redirect('staff_add_student')
                              
                              elif not username:
                                        messages.warning(request, 'Username is Required')
                                        return redirect('staff_add_student')

                              elif not addmission_no:
                                        messages.warning(request, 'Addmission Number is Required')
                                        return redirect('staff_add_student')

                              elif not address:
                                        messages.warning(request, 'Address is Required')
                                        return redirect('staff_add_student')

                              elif not mobile:
                                        messages.warning(request, 'Mobile Number is Required')
                                        return redirect('staff_add_student')

                              elif not father_name:
                                        messages.warning(request, 'Father Name is Required')
                                        return redirect('staff_add_student')

                              elif not mother_name:
                                        messages.warning(request, 'Mother Name is Required')
                                        return redirect('staff_add_student')

                              elif not parent_no:
                                        messages.warning(request, 'Parent Mobile Number is Required')
                                        return redirect('staff_add_student')

                              elif not password:
                                        messages.warning(request, 'Some Password is Required')
                                        return redirect('staff_add_student')
                                        
                              elif Login.objects.filter(email=email).exists():
                                        messages.warning(request, 'Email Already Exists')
                                        return redirect('staff_add_student')

                              else:
                                        
                                        user2 = Login(
                                                  first_name = first_name,
                                                  last_name = last_name,
                                                  email = email,
                                                  profile_pic = image,
                                                  user_type='3',
                                                  username=username,
                                                  password=password)
                                        user2.save()
                                        
                                        Student(
                                                  user=user2,
                                                  course_id=courses,
                                                  session_year_id=session_year,
                                                  addmission_no=addmission_no,
                                                  gender=gender,
                                                  address=address,
                                                  mobile=mobile,
                                                  dob=dob,
                                                  father_name=father_name,
                                                  mother_name=mother_name,
                                                  parent_mobile_no=parent_no,
                                                  admission_fees=admission_fees2).save()
                                        messages.success(request, user2.first_name + "  " + user2.last_name +  " Are Added Successfully")
                                        return redirect('staff_add_student')

                    else:
                              for c in admin:
                                        ft_name=c.first_name
                                        lt_name=c.last_name
                                        image=c.profile_pic

                                        addmission_no = random.randint(111111111,999999999)
                                        while Student.objects.filter(addmission_no = addmission_no) is None:
                                                  addmission_no = random.randint(111111111,999999999)
                                        addmission_no = addmission_no

                              data = {
                                        'first_name':ft_name,
                                        'last_name':lt_name,
                                        'image':image,
                                        'admin':admin,
                                        'course':course,
                                        'session':session,
                                        'error':error_message,
                                        'addmission_no':addmission_no
                              }
                              return render(request, 'staff/add_student.html',data)
          else:
                    return redirect('login')

#===========================================================================================
#===========================================================================================



#================================ Staff Manage Student =====================================

def staff_manage_student(request):
  if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        student = Student.objects.all().order_by('-created_date')
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'student':student,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
          }
        return render(request, 'staff/manage_student.html',data)
  else:
    return redirect('login')


#===========================================================================================
#===========================================================================================



#=============================== Staff View Student ========================================

def staff_view_student(request,pk):
  if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        student = Student.objects.filter(id=pk)
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'student':student,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
          }
        return render(request, 'staff/view_student.html',data)
  else:
    return redirect('login')

#===========================================================================================
#==========================================================================================



#================================== Staff Edit Student ======================================

def staff_edit_student(request,pk):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        student = Student.objects.filter(id=pk)
        course = Course.objects.all()
        session = Session.objects.all()
                    
        error_message = None
                    
        if request.method=="POST":
            student_id = request.POST["student_id"]
            first_name = request.POST["first_name"]
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            user_name = request.POST['user_name']
            address = request.POST['address']
            email_id = request.POST['email']
            mobile = request.POST['mobile_no']
            father_name = request.POST["father_name"]
            mother_name = request.POST["mother_name"]
            parent_no = request.POST["parent_no"]
            course_id = request.POST['course_id']
            session_id = request.POST['session_id']
            addmission_no = request.POST['addmission_no']
            dob = request.POST['dob']
            password = request.POST['password']
            admission_fees = request.POST['admission_fees']
            admission_fees2= int(admission_fees)


            usr = Login.objects.get(id=student_id)

            usr.username = user_name
            usr.first_name = first_name
            usr.last_name = last_name
            usr.email = email_id
            usr.password = password

            if len(request.FILES) != 0:
                    image = request.FILES['pic']
                    usr.profile_pic = image
            else:
                    pass

            usr2 = Student.objects.get(user=student_id)
            
            usr2.address = address
            usr2.mobile = mobile
            usr2.gender = gender
            usr2.addmission_no = addmission_no
            usr2.father_name = father_name
            usr2.mother_name = mother_name
            usr2.parent_mobile_no = parent_no
            usr2.dob = dob
            usr2.admission_fees = admission_fees2

            courses = Course.objects.get(id=course_id)
            session_year = Session.objects.get(id=session_id)
            usr2.course_id = courses
            usr2.session_year_id = session_year


            usr2.save()
            usr.save()
            messages.success(request, 'Details Updated Successfully')
            return redirect(f"/staff_edit_student{pk}")
                              
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
                'student':student,
                'course':course,
                'session':session
                }
            return render(request, 'staff/edit_student.html',data)
    else:
        return redirect('login')


#===========================================================================================
#===========================================================================================




#=================================== Staff Delete Student ==================================

def staff_delete_student(request,pk):
    if request.session.has_key('email'):
        admin = Login.objects.filter(id=pk)
        admin.delete()
        messages.warning(request, 'Student Delete Successfully')
        return redirect('staff_manage_student')
    else:
        return redirect('login')
       
#===========================================================================================
#===========================================================================================



#=========================== Staff Delete Student Profile Picture =========================

def staff_delete_student_picture(request,pk):
    if request.session.has_key('email'):
        admin = Login.objects.filter(id=pk)
        for c in admin:
            id=c.id
            image=c.profile_pic
            image.delete()
            user = Student.objects.filter(user=id)
            for ad in user:
                id2 = ad.id
            messages.warning(request, 'Image Delete Successfully')
            return redirect(f"/staff_edit_student{id2}")
    else:
        return redirect('login')


#===========================================================================================