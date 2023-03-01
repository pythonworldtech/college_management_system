from django.urls import path
from .main_views import*

#============================ Import Admin Functions ================================

from .views.admin.home import*
from .views.admin.edit_profile import*
from .views.admin.student import*
from .views.admin.staff import*
from .views.admin.course import*
from .views.admin.subject import*
from .views.admin.session import*
from .views.admin.student_attendance import*
from .views.admin.staff_attendance import*
from .views.admin.result import*
from .views.admin.notification import*
from .views.admin.leave import*
from .views.admin.admission import*
from .views.admin.contact_us import*
from .views.admin.student_fees import*
from .views.admin.student_proceed_to_pay import*
from .views.admin.staff_proceed_to_pay import*
from .views.admin.staff_salary import*
from .views.admin.account_setting import*


#====================================================================================


#============================ Import Staff Functions ================================

from .views.staff.home import*
from .views.staff.result import*
from .views.staff.student import*
from .views.staff.attendance import*
from .views.staff.notification import*
from .views.staff.leave import*
from .views.staff.edit_profile import*
from .views.staff.student_fees import*
from .views.staff.proceed_to_pay import*
from .views.staff.staff_salary import*
from .views.staff.student_notes import*
from .views.staff.account_setting import*


#======================================================================================

#============================ Import Student Functions ================================

from .views.student.home import*
from .views.student.notification import*
from .views.student.leave import*
from .views.student.result import*
from .views.student.attendance import*
from .views.student.edit_profile import*
from .views.student.proceed_to_pay import*
from .views.student.fees import*
from .views.student.notes import*
from .views.student.account_setting import*

#=======================================================================================

urlpatterns = [
          path('',index,name='index'),
          path('about',about,name='about'),
          path('course',course,name='course'),
          path('join',join,name='join'),
          path('gallery',gallery,name='gallery'),
          path('contact',contact,name='contact'),
          path('login',Login_view.as_view(),name='login'),
          path('dologout',dologout,name='dologout'),
          path('admission',admission,name='admission'),
          path('application',application_status,name='application'),
          path('search',application_search,name='search'),
          path('forgot_password',forgot_password,name='forgot_password'),
          path('send_otp',send_otp,name='send_otp'),
          path('enter_otp',enter_otp,name='enter_otp'),
          path('password_reset',password_reset,name='password_reset'),

          #=================================================================================
          #=================================================================================

          #=========================Admin===================================================
          
          path('admin_home',admin_home,name='admin_home'),
          path('admin_edit_profile',edit_profile,name='edit_profile'),
          path('admin_change_email', admin_change_email, name='admin_change_email'),
          path('admin_change_password', admin_change_password, name='admin_change_password'),

          path('admin_add_student',admin_add_student,name='admin_add_student'),
          path('admin_manage_student',admin_manage_student,name='admin_manage_student'),
          path('admin_view_student<int:pk>',admin_view_student,name='admin_view_student'),
          path('admin_edit_student<int:pk>',admin_edit_student,name='admin_edit_student'),
          path('admin_delete_student_picture<int:pk>',admin_delete_student_picture,name='admin_delete_student_picture'),
          path('admin_delete_student<int:pk>',admin_delete_student,name='admin_delete_student'),
          

          path('admin_add_staff',admin_add_staff,name='admin_add_staff'),
          path('admin_manage_staff',admin_manage_staff,name='admin_manage_staff'),
          path('admin_view_staff<int:pk>',admin_view_staff,name='admin_view_staff'),
          path('admin_edit_staff<int:pk>',admin_edit_staff,name='admin_edit_staff'),
          path('admin_delete_staff_picture<int:pk>',admin_delete_staff_picture,name='admin_delete_staff_picture'),
          path('admin_delete_staff<int:pk>',admin_delete_staff,name='admin_delete_staff'),

          path('admin_add_course',admin_add_course,name='admin_add_course'),
          path('admin_manage_course',admin_manage_course,name='admin_manage_course'),
          path('admin_edit_course<int:pk>',admin_edit_course,name='admin_edit_course'),
          path('admin_delete_course<int:pk>',admin_delete_course,name='admin_delete_course'),

          path('admin_add_subject',admin_add_subject,name='admin_add_subject'),
          path('admin_manage_subject',admin_manage_subject,name='admin_manage_subject'),
          path('admin_edit_subject<int:pk>',admin_edit_subject,name='admin_edit_subject'),
          path('admin_delete_subject<int:pk>',admin_delete_subject,name='admin_delete_subject'),

          path('admin_add_session',admin_add_session,name='admin_add_session'),
          path('admin_manage_session',admin_manage_session,name='admin_manage_session'),
          path('admin_edit_session<int:pk>',admin_edit_session,name='admin_edit_session'),
          path('admin_delete_session<int:pk>',admin_delete_session,name='admin_delete_session'),


          path('admin_take_student_attendance',admin_take_student_attendance,name='admin_take_student_attendance'),
          path('admin_save_student_attendance',admin_save_student_attendance,name='admin_save_student_attendance'),
          path('admin_view_student_attendance',admin_view_student_attendance,name='admin_view_student_attendance'),
          path('admin_delete_student_attendance<int:pk>',admin_delete_student_attendance,name='admin_delete_student_attendance'),


          path('admin_add_result',admin_add_result,name='admin_add_result'),
          path('admin_save_result',admin_save_result,name='admin_save_result'),
          path('admin_view_result',admin_view_result,name='admin_view_result'),
          path('admin_edit_result<int:pk>',admin_edit_result,name='admin_edit_result'),
          path('admin_delete_result<int:pk>',admin_delete_result,name='admin_delete_result'),


          path('admin_save_staff_attendance',admin_save_staff_attendance,name='admin_save_staff_attendance'),
          path('admin_view_staff_attendance',admin_view_staff_attendance,name='admin_view_staff_attendance'),
          path('admin_delete_staff_attendance<int:pk>',admin_delete_staff_attendance,name='admin_delete_staff_attendance'),

          
          

          path('admin_send_staff_notification',admin_send_staff_notification,name='admin_send_staff_notification'),
          path('admin_save_staff_notification',admin_save_staff_notification,name='admin_save_staff_notification'),
          path('admin_send_student_notification',admin_send_student_notification,name='admin_send_student_notification'),
          path('admin_save_student_notification',admin_save_student_notification,name='admin_save_student_notification'),


          path('admin_view_staff_leave',admin_view_staff_leave,name='admin_view_staff_leave'),
          path('admin_staff_leave_approve/<leave_id>/', admin_staff_leave_approve, name="admin_staff_leave_approve"),
          path('admin_staff_leave_reject/<leave_id>/', admin_staff_leave_reject, name="admin_staff_leave_reject"),

          path('admin_view_student_leave',admin_view_student_leave,name='admin_view_student_leave'),
          path('admin_student_leave_approve/<leave_id>/', admin_student_leave_approve, name="admin_student_leave_approve"),
          path('admin_student_leave_reject/<leave_id>/', admin_student_leave_reject, name="admin_student_leave_reject"),

          path('admin_view_admission',admin_view_admission,name='admin_view_admission'),
          path('admin_admission_approve/<admission_id>/', admin_admission_approve, name="admin_admission_approve"),
          path('admin_admission_reject/<admission_id>/', admin_admission_reject, name="admin_admission_reject"),

          path('admin_view_contact_us',admin_view_contact_us,name='admin_view_contact_us'),

          path('admin_view_student_fees',admin_view_student_fees,name='admin_view_student_fees'),
          path('admin_proceed-to-pay', admin_proceed_to_pay, name='admin_proceed-to-pay'),
          path('admin_view_student_fees_receipt',admin_view_student_fees_receipt,name='admin_view_student_fees_receipt'),
          path('admin_student_fees_receipt<int:pk>',admin_student_fees_receipt,name='admin_student_fees_receipt'),
          
          

          path('admin_view_staff_salary',admin_view_staff_salary,name='admin_view_staff_salary'),
          path('admin_proceed-to-pay2', admin_proceed_to_pay2, name='admin_proceed-to-pay2'),
          path('admin_view_staff_salary_receipt',admin_view_staff_salary_receipt,name='admin_view_staff_salary_receipt'),
          path('admin_staff_salary_receipt<int:pk>',admin_staff_salary_receipt,name='admin_staff_salary_receipt'),

          #==================================================================================
          #==================================================================================





          #================================ Staff ===========================================

          path('staff_home',staff_home,name='staff_home'),
          path('staff_edit_profile',staff_edit_profile,name='staff_edit_profile'),


          path('staff_add_student',staff_add_student,name='staff_add_student'),
          path('staff_manage_student',staff_manage_student,name='staff_manage_student'),
          path('staff_view_student<int:pk>',staff_view_student,name='staff_view_student'),
          path('staff_edit_student<int:pk>',staff_edit_student,name='staff_edit_student'),
          path('staff_delete_student_picture<int:pk>',staff_delete_student_picture,name='staff_delete_student_picture'),
          path('staff_delete_student<int:pk>',staff_delete_student,name='staff_delete_student'),


          path('staff_add_result',staff_add_result,name='staff_add_result'),
          path('staff_save_result',staff_save_result,name='staff_save_result'),
          path('staff_view_result',staff_view_result,name='staff_view_result'),
          path('staff_edit_result<int:pk>',staff_edit_result,name='staff_edit_result'),
          path('staff_delete_result<int:pk>',staff_delete_result,name='staff_delete_result'),


          path('staff_take_attendance',staff_take_attendance,name='staff_take_attendance'),
          path('staff_save_attendance',staff_save_student_attendance,name='staff_save_attendance'),
          path('staff_view_student_attendance',staff_view_student_attendance,name='staff_view_student_attendance'),
          path('staff_view_attendance',staff_view_attendance,name='staff_view_attendance'),
          

          path('staff_notification',staff_notification,name='staff_notification'),
          path('staff_read_notification/<str:status>',staff_read_notification,name='staff_read_notification'),

          path('staff_apply_leave',staff_apply_leave,name='staff_apply_leave'),
          path('staff_save_leave',staff_save_leave,name='staff_save_leave'),

          path('staff_view_student_fees',staff_view_student_fees,name='staff_view_student_fees'),
          path('staff_proceed-to-pay', staff_proceed_to_pay, name='staff_proceed-to-pay'),
          path('staff_view_student_fees_receipt',staff_view_student_fees_receipt,name='staff_view_student_fees_receipt'),
          path('staff_student_fees_receipt<int:pk>',staff_student_fees_receipt,name='staff_student_fees_receipt'),
          

          path('staff_view_salary_receipt',staff_view_staff_salary_receipt,name='staff_view_salary_receipt'),
          path('staff_salary_receipt<int:pk>',staff_salary_receipt,name='staff_salary_receipt'),

          path('staff_student_notes',staff_student_notes,name='staff_student_notes'),
          path('staff_student_notes_approve/<notes_id>/', staff_student_notes_approve, name="staff_student_notes_approve"),
          path('staff_student_notes_reject/<notes_id>/', staff_student_notes_reject, name="staff_student_notes_reject"),
          path('staff_notes_reply',staff_notes_reply,name='staff_notes_reply'),

          path('staff_change_email', staff_change_email, name='staff_change_email'),
          path('staff_change_password', staff_change_password, name='staff_change_password'),
          
          #===================================================================================
          #===================================================================================


          
          
          
          #=========================== Student ===============================================

          path('student_home',student_home,name='student_home'),

          path('student_notification',student_notification,name='student_notification'),
          path('student_read_notification/<str:status>',student_read_notification,name='student_read_notification'),

          path('student_apply_leave',student_apply_leave,name='student_apply_leave'),
          path('student_save_leave',student_save_leave,name='student_save_leave'),

          path('student_view_result',student_view_result,name='student_view_result'),

          path('student_view_attendance',student_view_attendance,name='student_view_attendance'),

          path('student_edit_profile',student_edit_profile,name='student_edit_profile'),

          path('student_fees',student_fees,name='student_fees'),
          path('proceed-to-pay', proceed_to_pay, name='proceed-to-pay'),

          path('student_fees_receipt<int:pk>',student_fees_receipt,name='student_fees_receipt'),

          path('student_notes', student_notes, name='student_notes'),
          path('student_submit_notes', student_submit_notes, name='student_submit_notes'),

          path('student_change_email', student_change_email, name='student_change_email'),
          path('student_change_password', student_change_password, name='student_change_password'),

          #================================================================================
          #================================================================================

]
