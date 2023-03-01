#==================================== Import ==============================================

from django.shortcuts import render, redirect
from django.contrib import messages
from college.models.login import Login
#===========================================================================================


#============================== Admin Edit Profile =========================================

def edit_profile(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    user = Login.objects.filter(email=email)
                    user2 = Login.objects.get(email=email)
                    
                    for c in user:
                              first_name=c.first_name
                              last_name=c.last_name
                              image=c.profile_pic

                              if request.method == 'POST':
                                        first_name = request.POST['fname']
                                        last_name = request.POST['lname']

                                        if len(request.FILES) != 0:
                                                  picture = request.FILES["pic"]
                                                  user2.profile_pic = picture
                                                  user2.save()
                                        else:
                                                  pass

                                        user2.first_name = first_name
                                        user2.last_name = last_name
                                        user2.save()
                                        messages.success(request,'Details Updated Successfully')
                                        return redirect('edit_profile')
            
                              data = {
                                        'first_name':first_name,
                                        'last_name':last_name,
                                        'image':image,
                                        'admin':user
                              }
                    return render(request, 'admin/edit_profile.html',data)
          else:
                    return redirect('login')

#============================================================================================