#======================== Import ====================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from django.contrib import messages

#=====================================================================


#======================== Student Edit Profile =======================

def student_edit_profile(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    user = Login.objects.filter(email=email)
                    user2 = Login.objects.get(email=email)
                    
                    for c in user:
                              id = c.id
                              first_name=c.first_name
                              last_name=c.last_name
                              image=c.profile_pic
                    
                              student = Student.objects.filter(user=id)
                              student2 = Student.objects.get(user=id)

                              if request.method == 'POST':
                                        first_name = request.POST.get("fname")
                                        last_name = request.POST.get("lname")
                                        email = request.POST.get("eml")
                                        add = request.POST.get("address")
                                        dob = request.POST.get("dob")
                                        mbl = request.POST.get("mobile")
                                        ft_name = request.POST.get("father_name")
                                        mt_name = request.POST.get("mother_name")
                                        pt_no = request.POST["parent_no"]

                                        if len(request.FILES) != 0:
                                                  picture = request.FILES["pic"]
                                                  user2.profile_pic = picture
                                                  user2.save()
                                        else:
                                                  pass

                                        user2.first_name = first_name
                                        user2.last_name = last_name
                                        student2.address = add
                                        student2.dob = dob
                                        student2.mobile = mbl
                                        student2.father_name = ft_name
                                        student2.mother_name = mt_name
                                        student2.parent_mobile_no = pt_no
                                        user2.save()
                                        student2.save()
                                        messages.success(request, 'Details Updated Successfully')
                                        return redirect('student_edit_profile')
            
                              data = {
                                        'first_name':first_name,
                                        'last_name':last_name,
                                        'image':image,
                                        'admin':user,
                                        'student':student,
                                        
                              }
                    return render(request, 'student/edit_profile.html',data)
          else:
                    return redirect('login')
