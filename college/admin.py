#================================ Import Models ===========================================

from django.contrib import admin
from .models.events import Event
from .models.user import CustomeUser
from .models.login import Login
from .models.student import Student
from .models.staff import Staff
from .models.course import Course
from .models.session import Session
from .models.login import Login
from .models.subject import Subject
from django.contrib.auth.admin import UserAdmin
from .models.attandance import Student_Attendance
from .models.attandance_report import Student_Attendance_Report
from .models.attandance import Staff_Attendance
from .models.result import Result
from .models.notification import *
from .models.leave import *
from .models.admission import Admission
from .models.contact_us import Contact_Us
from .models.gallery import Gallery
from .models.fees_receipt import Student_fees_Receipt
from .models.salary_receipt import Staff_salary_Receipt
from .models.student_note import Student_Note
#===========================================================================================
#===========================================================================================




#==================================== List Display =========================================
#==================================== xxxxxxxxxxxx =========================================


#================================ Event ===================================================

class AdminEvent(admin.ModelAdmin):
    list_display = ['id','name','event_date','event_place','created_date']

#=========================================================================================


#================================ Custome User ============================================

class AdminCustomeUser(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','user_type','profile_pic']

#==========================================================================================


#================================ Login ===================================================

class AdminLogin(admin.ModelAdmin):
    list_display = ['id','username','user_type','first_name','last_name','email',
                    'profile_pic','password']

#=========================================================================================


#================================ Student =================================================
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','user','addmission_no','course_id','session_year_id','address',
    'mobile','gender','dob','father_name','mother_name','parent_mobile_no','admission_fees',
    'paid_amount','created_date']

#=========================================================================================


#================================ Staff ==================================================
class AdminStaff(admin.ModelAdmin):
    list_display = ['id','stf_id','user','dob','address','mobile_number','gender',
    'account_no','ifsc_code','salary','paid_salary','created_date']

#=========================================================================================


#================================ Course ==================================================

class AdminCourse(admin.ModelAdmin):
    list_display = ['id','course_id','course_name','course_pic','course_description','created_date']

#=========================================================================================


#================================ Subject ================================================

class AdminSubject(admin.ModelAdmin):
    list_display = ['id','subject_id','subject_name','course','staff','created_date']

#=========================================================================================


#================================ Session ================================================

class AdminSession(admin.ModelAdmin):
    list_display = ['id','session_start','session_end','created_date']

#=========================================================================================


#================================ Result =================================================

class AdminResult(admin.ModelAdmin):
    list_display = ['id','student_id','subject_id','session_id','internal_marks',
    'external_marks','total_marks','created_date']

#=========================================================================================


#================================ Student_Attendance ======================================

class AdminStudent_Attendance(admin.ModelAdmin):
    list_display = ['id','subject_id','session_year','attendance_date','created_date']

#=========================================================================================


#============================== Student_Attendance_Report =================================

class AdminStudent_Attendance_Report(admin.ModelAdmin):
    list_display = ['id','student_id','attendance_id','created_date']

#=========================================================================================


#============================== Staff_Attendance =========================================

class AdminStaff_Attendance(admin.ModelAdmin):
    list_display = ['id','staff_id','attendance_date','created_date']

#=========================================================================================


#============================== Staff_Notification ========================================

class AdminStaff_notification(admin.ModelAdmin):
    list_display = ['id','staff_id','message','created_date']

#==========================================================================================


#============================== Student_Notification =====================================

class AdminStudent_notification(admin.ModelAdmin):
    list_display = ['id','student_id','message','created_date']

#=========================================================================================


#============================== Student_Notes =============================================

class AdminStudent_Notes(admin.ModelAdmin):
    list_display = ['id','student_id','staff_id','subject_id','topic','notes','reply','created_date']

#==========================================================================================

admin.site.register(Event, AdminEvent)
admin.site.register(CustomeUser, AdminCustomeUser)
admin.site.register(Student, AdminStudent)
admin.site.register(Staff,AdminStaff)
admin.site.register(Login, AdminLogin)
admin.site.register(Course, AdminCourse)
admin.site.register(Session, AdminSession)
admin.site.register(Subject, AdminSubject)
admin.site.register(Student_Attendance,AdminStudent_Attendance)
admin.site.register(Result,AdminResult)
admin.site.register(Student_Attendance_Report,AdminStudent_Attendance_Report)
admin.site.register(Staff_Attendance,AdminStaff_Attendance)
admin.site.register(Student_fees_Receipt)
admin.site.register(Staff_salary_Receipt)
admin.site.register(Staff_notification,AdminStaff_notification)
admin.site.register(Student_notification,AdminStudent_notification)
admin.site.register(Student_Leave)
admin.site.register(Staff_Leave)
admin.site.register(Admission)
admin.site.register(Contact_Us)
admin.site.register(Gallery)
admin.site.register(Student_Note,AdminStudent_Notes)



