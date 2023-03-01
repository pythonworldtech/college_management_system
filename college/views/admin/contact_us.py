#==================================== Import =============================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.contact_us import Contact_Us
#==========================================================================================


#========================= Admin Contact Us ================================================

def admin_view_contact_us(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)
                    contact_us = Contact_Us.objects.all()
                    
                    data = {
                              'admin':admin,
                              'contact':contact_us
                    }
                    return render(request, 'admin/contact_us.html',data)
          else:
                    return redirect('login')


#========================================================================================