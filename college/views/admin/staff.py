#==================================== Import ============================================

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
import random
from college.models.staff import Staff
from college.models.login import Login
from college.models.course import Course
#==========================================================================================



#==================================== Admin Add Staff ======================================

def admin_add_staff(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        course_name = Course.objects.all()
                    
        error_message = None
        
        if request.method=="POST":
            first_name = request.POST["first_name"]
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            user_name = request.POST['user_name']
            address = request.POST['address']
            email_id = request.POST['email']
            mobile = request.POST['mobile_no']
            image = request.FILES['pic']
            password = request.POST['password']
            name = request.POST['name']
            dob = request.POST['dob']
            account_no = request.POST['account_no']
            ifsc_code = request.POST['ifsc_code']
            salary_paid = request.POST['salary']
            salary = int(salary_paid)


            value = {
                'first_name' : first_name,
                'last_name' : last_name,
                'mobile' : mobile,
                'email' : email_id,
                'username':user_name,
                'address':address,
                'gender':gender,
                }
                
            if Login.objects.filter(username=user_name).exists():
                messages.warning(request, 'Username Already Exists')
                return redirect('admin_add_staff')
                
            if(not first_name ):
                messages.warning(request, 'First Name is Required')
                return redirect('admin_add_staff')
                
            elif len(mobile) < 10:
                messages.warning(request, 'Mobile Number must be 10 Character long')
                return redirect('admin_add_staff') 
            
            elif not last_name:
                messages.warning(request, 'Last Name is Required')
                return redirect('admin_add_staff')

            elif not gender:
                messages.warning(request, 'Please Select the Gender')
                return redirect('admin_add_staff')


            elif not user_name:
                messages.warning(request, 'Username is Required')
                return redirect('admin_add_staff')

            elif not address:
                messages.warning(request, 'Address is Required')
                return redirect('admin_add_staff')

            elif not email_id:
                messages.warning(request, 'Email Address is Required')
                return redirect('admin_add_staff')

            elif not mobile:
                messages.warning(request, 'Mobile Number is Required')
                return redirect('admin_add_staff')
                              
            elif not password:
                messages.warning(request, 'Some Password is Required')
                return redirect('admin_add_staff')
                              
            elif Login.objects.filter(email=email_id).exists():
                messages.warning(request, 'Email Already Exists')
                return redirect('admin_add_staff')
                              
            else:
                
                    user = Login(first_name = first_name,last_name = last_name,email = email_id,profile_pic = image,user_type='2',username=user_name,password=password)
                    user.save()
                    Staff(
                        dob=dob,
                        stf_id=name,
                        user=user,
                        address=address,
                        gender=gender,
                        mobile_number=mobile,
                        account_no = account_no,
                        ifsc_code=ifsc_code,
                        salary=salary).save()
                    messages.success(request, user.first_name + "  " + user.last_name +  " Are Added Successfully")
                    return redirect('admin_add_staff')
        else:
            
            for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic

                staffs = ['STAFF']
                staff_ids =f'{random.choice(staffs)}-0{random.randint(100,999)}'
                while Staff.objects.filter(stf_id = staff_ids) is None:
                    staff_ids =f'{random.choice(staffs)}-0{random.randint(100,999)}'
                    staff_ids = staff_ids
                
                data = {
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image,
                    'admin':admin,
                    'error':error_message,
                    'course':course_name,
                    'staff_id':staff_ids
                }
                return render(request, 'admin/add_staff.html',data)
    else:
        return redirect('login')

#============================================================================================



#=================================== Admin Manage Staff =====================================

def admin_manage_staff(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        staff = Staff.objects.all().order_by('-created_date')
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'staff':staff,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
        }
        return render(request, 'admin/manage_staff.html',data)
    else:
        return redirect('login')

#=============================================================================================



#=============================== Admin View Staff ==========================================

def admin_view_staff(request,pk):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        staff = Staff.objects.filter(id=pk)
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'staff':staff,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
        }
        return render(request, 'admin/view_staff.html',data)
    else:
        return redirect('login')

#===========================================================================================



#============================= Admin Edit Staff ============================================

def admin_edit_staff(request,pk):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        staff = Staff.objects.filter(id=pk)
                    
        error_message = None
                    
        if request.method=="POST":
            staff_id = request.POST["staff_id"]
            first_name = request.POST["first_name"]
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            user_name = request.POST['user_name']
            address = request.POST['address']
            email_id = request.POST['email']
            mobile = request.POST['mobile_no']
            password = request.POST['password']
            account_no = request.POST['account_no']
            ifsc_code = request.POST['ifsc_code']
            salary_paid = request.POST['salary']
            salary = int(salary_paid)
            usr = Login.objects.get(id=staff_id)

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
            
            usr2 = Staff.objects.get(user=staff_id)
            usr2.address = address
            usr2.mobile_number = mobile
            usr2.gender = gender
            usr2.account_no = account_no
            usr2.ifsc_code = ifsc_code
            usr2.salary = salary

            usr2.save()
            usr.save()
            messages.success(request, 'Details Updated Successfully')
            return redirect(f"/admin_edit_staff{pk}")
                              
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
                'staff':staff
                }
            return render(request, 'admin/edit_staff.html',data)
    else:
        return redirect('login')

#===========================================================================================



#=========================================== Admin Delete Staff =============================

def admin_delete_staff(request,pk):
    if request.session.has_key('email'):
        admin = Login.objects.filter(id=pk)
        admin.delete()
        messages.warning(request, 'Staff Delete Successfully')
        return redirect('admin_manage_staff')
    else:
        return redirect('login')
       
#============================================================================================



#==================================== Admin Delete Staff Picture ============================

def admin_delete_staff_picture(request,pk):
    if request.session.has_key('email'):
        admin = Login.objects.filter(id=pk)
        for c in admin:
            id=c.id
            image=c.profile_pic
            image.delete()
            user = Staff.objects.filter(user=id)
            for ad in user:
                id2 = ad.id
            messages.warning(request, 'Image Delete Successfully')
            return redirect(f"/admin_edit_staff{id2}")
    else:
        return redirect('login')
       
#============================================================================================