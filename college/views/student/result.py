#======================== Import ===========================================================

from django.shortcuts import render, redirect
from college.models.login import Login
from college.models.student import Student
from college.models.result import Result

#==========================================================================================

#======================== Student Result ==================================================

def student_view_result(request):
          if request.session.has_key('email'):
                    email = request.session["email"]
                    admin = Login.objects.filter(email=email)

                    for a in admin:
                              id = a.id

                    total = None
                    
                    student = Student.objects.filter(user=id)
                    for st in student:
                              student_id = st.id
                              result = Result.objects.filter(student_id=student_id)

                              

                              for re in result:
                                        total = re.total_marks
                                        
                    data = {
                              'admin':admin,
                              'result':result,
                              'total':total
                    }
                    return render(request, 'student/student_view_result.html',data)
          else:
                    return redirect('login')


#============================================================================================