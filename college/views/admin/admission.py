#==================================== Import ============================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.admission import Admission
#========================================================================================


#============================= Admin View Admission Form =================================

def admin_view_admission(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        admin = Login.objects.filter(email=email)
        admission = Admission.objects.all()

        data = {
            'admin':admin,
            'admission':admission
        }

        return render(request, 'admin/view_admission.html',data)
    else:
        return redirect('login')

#========================================================================================



#============================== Admin Approved Admission Form ============================

def admin_admission_approve(request, admission_id):
    if request.session.has_key('email'):
        admission = Admission.objects.get(id=admission_id)
        admission.status = 1
        admission.save()
        return redirect('admin_view_admission')
    else:
        return redirect('login')

#==========================================================================================


#============================== Admin Reject Admission Form ===============================

def admin_admission_reject(request, admission_id):
    if request.session.has_key('email'):
        admission = Admission.objects.get(id=admission_id)
        admission.status = 2
        admission.save()
        return redirect('admin_view_admission')
    else:
        return redirect('login')


#============================================================================================