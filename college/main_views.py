#=================================== Import ================================================

from distutils.log import Log
from college.models.course import Course
from college.models.gallery import Gallery
from django.views import  View
from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.login import Login
from college.models.admission import Admission
from college.models.contact_us import Contact_Us
import random
import time
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
#===========================================================================================



#================================== Index Page =============================================

def index(request):
    return render(request, 'index.html')

#===========================================================================================


#================================== About Page =============================================

def about(request):
    return render(request, 'about.html')

#===========================================================================================


#=================================== Course Page ===========================================

def course(request):
    course = Course.objects.all().order_by('-created_date')
    data = {
        'course':course
    }
    return render(request, 'courses.html',data)

#===========================================================================================


#=================================== Join Page =============================================

def join(request):
    course = Course.objects.all()
    application = ['APPLICATION']
    application_no =f'{random.choice(application)}-0{random.randint(10000,99999)}'
    while Admission.objects.filter(application_no = application_no) is None:
        application_no =f'{random.choice(application)}-0{random.randint(10000,99999)}'
        application_no = application_no
    return render(request, 'join.html',{'course':course,'application_no':application_no})

#============================================================================================



#==================================== Gallery Page =========================================

def gallery(request):
    gallery = Gallery.objects.all().order_by('-created_date')
    data = {
        'gallery':gallery
    }
    return render(request, 'gallery.html',data)

#===========================================================================================



#==================================== Contact Page =========================================

def contact(request):
    if request.method=="POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone")
        message = request.POST.get("message")
        reference = ['REF']
        reference_no =f'{random.choice(reference)}-0{random.randint(1000000000,9999900000)}'
        while Contact_Us.objects.filter(reference_no = reference_no) is None:
            reference_no =f'{random.choice(reference)}-0{random.randint(1000000000,9999900000)}'
            reference_no = reference_no


        Contact_Us(
            reference_no=reference_no,
            full_name = full_name,
            email = email,
            phone = phone_no,
            message = message
        ).save()
        return redirect('contact')
    else:
        return render(request, 'contact.html')

#===========================================================================================



#==================================== Reset Password Page ==================================

def forgot_password(request):
    return render(request,'forgot_password.html')
    



def send_otp(request):
    error_message = None
    otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
    email = request.POST.get('email')
    user2 = Login.objects.filter(email=email)
    if user2:
        user = Login.objects.get(email=email)
        user.otp = otp
        user.save()
        request.session['email']=request.POST["email"]
        mydict = {'otp': otp}
        html_template = 'forgot_email.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = 'Welcome to Python World'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        return redirect('enter_otp')
    else: 
        error_message = "Invalid Email Please Enter Correct Email !!"
        return render(request,'forgot_password.html',{'error':error_message})

    


def enter_otp(request):
    error_message = None
    if request.session.has_key('email'):
                    email = request.session["email"]
                    user = Login.objects.filter(email=email)
                    user2 = Login.objects.get(email=email)
                    for u in user:
                        user_otp = u.otp
                    if request.method == 'POST':
                        otp = request.POST.get('otp')
                        if(not otp ):
                            error_message = "OTP is Required !!"
                        elif not user_otp==otp:
                            error_message = "Enter OTP is Invalid"
                        if not error_message:
                            return redirect('password_reset')
                    return render(request,'enter_otp.html',{'error':error_message})


def password_reset(request):
    error_message = None
    if request.session.has_key('email'):
                    email = request.session["email"]
                    user2 = Login.objects.get(email=email)
                    if request.method == 'POST':
                        new_password = request.POST.get('npassword')
                        cnew_password = request.POST.get('cnpassword')
                        if(not new_password ):
                            error_message = "Enter New Password"
                        elif not cnew_password:
                            error_message = "Enter Confirm New Password !!"
                        elif not new_password == cnew_password :
                            error_message = "Password & Confirm Password Should be Same !!"
                        if not error_message:
                            messages.success(request, 'Password Changed Successfully')
                            user2.password = new_password
                            user2.save()
    return render(request,'password_reset.html')

#===========================================================================================
#===========================================================================================



#====================================== Applicaion Status Page =============================

def application_status(request):
    application = Admission.objects.all()
    data = {
        'application':application
    }
    return render(request, 'application_status.html',data)

#============================================================================================



#=================================== Application Search Page ================================

def application_search(request):
    application = Admission.objects.all()
    query = request.GET.get('query')
    search = Admission.objects.filter(application_no=query)
    data = {
        'search':search,
        'query':query,
        'application':application
    }
    return render(request, 'application_status.html',data)

#===========================================================================================



#======================================= Login Page =========================================

class Login_view(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Login.get_customer_by_email(email)
        if user:
            request.session['email']=request.POST["email"]
                
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
                return redirect('staff_home')
                
            elif user_type == '3':
                return redirect('student_home')
                
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')

        else: 
            messages.error(request, "Invalid Email or Password !!")
            return redirect('login')
        
#===========================================================================================



#======================================== Logout Page ======================================

def dologout(request):
    if request.session.has_key('email'):
        del request.session["email"]
        return redirect('login')
    else:
        return redirect('login')

#============================================================================================



#==================================== Admission Page ========================================

def admission(request):
    if request.method=="POST":
        application_no = request.POST.get("application_no")
        full_name = request.POST.get("full_name")
        father_name = request.POST.get("fname")
        mother_name = request.POST.get("mname")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone")
        course = request.POST.get("course")
        address = request.POST.get("address")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip_code")

        get_course = Course.objects.get(id=course)

        Admission(
            application_no = application_no,
            full_name = full_name,
            father_name = father_name,
            mother_name = mother_name,
            dob = dob,
            gender = gender,
            email = email,
            phone = phone_no,
            course = get_course,
            address = address,
            state = state,
            city = city,
            zip_code = zip_code
        ).save()
        mydict = {'name': full_name,'application_no':application_no}
        html_template = 'application_email.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = 'Welcome to Python World'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        return redirect('join')
 
#============================================================================================