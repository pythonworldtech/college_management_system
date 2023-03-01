#================================= Import =================================================


from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.login import Login
from college.models.staff import Staff

#==========================================================================================

#==================================== Staff Edit Profile ==================================

def staff_edit_profile(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    user = Login.objects.filter(email=email)
                    user2 = Login.objects.get(email=email)
                    
                    for c in user:
                              id=c.id
                              first_name=c.first_name
                              last_name=c.last_name
                              image=c.profile_pic
                              
                              staff = Staff.objects.filter(user=id)
                              staff2 = Staff.objects.get(user=id)

                              if request.method == 'POST':
                                        first_name = request.POST.get("fname")
                                        last_name = request.POST.get("lname")
                                        email = request.POST.get("eml")
                                        add = request.POST.get("address")
                                        dob = request.POST.get("dob")
                                        mbl = request.POST.get("mobile")

                                        if len(request.FILES) != 0:
                                                  picture = request.FILES["pic"]
                                                  user2.profile_pic = picture
                                                  user2.save()
                                        else:
                                                  pass

                                        user2.first_name = first_name
                                        user2.last_name = last_name
                                        staff2.address = add
                                        staff2.dob = dob
                                        staff2.mobile_number = mbl
                                        user2.save()
                                        staff2.save()
                                        messages.success(request, 'Details Updated Successfully')
                                        return redirect('staff_edit_profile')
            
                              data = {
                                        'first_name':first_name,
                                        'last_name':last_name,
                                        'image':image,
                                        'admin':user,
                                        'staff':staff
                              }
                    return render(request, 'staff/edit_profile.html',data)
          else:
                    return redirect('login')

#==========================================================================================
#==========================================================================================