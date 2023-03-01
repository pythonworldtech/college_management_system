#==================================== Import ================================================

from django.contrib import messages
from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.session import Session
#===========================================================================================



#================================= Admin Add Session =======================================

def admin_add_session(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    if request.method=="POST":
                              session_start = request.POST.get("session_start")
                              session_end = request.POST.get("session_end")
                              
                              session = Session(
                                        session_start = session_start,
                                        session_end = session_end
                              )
                              session.save()
                              messages.success(request, 'Session Added Successfully')
                              return redirect('admin_add_session')
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
                              }
                              return render(request, 'admin/add_session.html',data)
          else:
                    return redirect('login')

#===========================================================================================



#===================================== Admin Manage Session =================================

def admin_manage_session(request):
  if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        session = Session.objects.all().order_by('-created_date')
        for c in admin:
                ftname=c.first_name
                ltname=c.last_name
                image=c.profile_pic
        data = {
                    'session':session,
                    'admin':admin,
                    'first_name':ftname,
                    'last_name':ltname,
                    'image':image
          }
        return render(request, 'admin/manage_session.html',data)
  else:
    return redirect('login')

#===========================================================================================



#=================================== Admin Edit Session ====================================

def admin_edit_session(request,pk):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        session = Session.objects.filter(id=pk)

        for c in session:
                  id = c.id
                    
        error_message = None
                    
        if request.method=="POST":
            session_start = request.POST['session_start']
            session_end = request.POST['session_end']
            
            update_session = Session.objects.get(id=id)
            update_session.session_start = session_start
            update_session.session_end = session_end
            update_session.save()
            messages.success(request, 'Session Updated Successfully')
            return redirect(f"/admin_edit_session{pk}")
                              
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
                'session':session
                }
            return render(request, 'admin/edit_session.html',data)
    else:
        return redirect('login')

#===========================================================================================



#================================= Admin Delete Session =====================================

def admin_delete_session(request,pk):
    if request.session.has_key('email'):
        session = Session.objects.filter(id=pk)
        session.delete()
        messages.warning(request, 'Session Delete Successfully')
        return redirect('admin_manage_session')
    else:
        return redirect('login')

#============================================================================================