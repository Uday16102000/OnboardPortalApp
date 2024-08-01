from django.shortcuts import render,redirect
from onboardportalapp.models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.

# def signIn(username,password):


def landingPage(request):
    # user=get_object_or_404(User)
    return render(request,"onboardportalapp/signIn.html",{"message":"Please Sign In Using Admin Credential"})


def signIn(request):

    try:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(user_name=username, password=password)
    except(User.DoesNotExist):
         messages.error(request, "Invalid username or password.")
         return redirect('/onboard')
    
    branch_list=Branch.objects.all()
    print("branch",branch_list)
    
         

    return render(request,"onboardportalapp/branch.html",{"message":"Please Select The Branch For Detail Information","branch_list":branch_list})



def addBranch(request):

    branchName=request.POST.get("branch")
    if branchName:
       branch=Branch()
       branch.branch_name=branchName
       branch.save()
       message='Branch added successfully'
    else:
       message='Branch name cannnot be empty'

    branch_list=Branch.objects.all()
    print("branch",branch_list)
    return render(request, "onboardportalapp/branch.html", {"branch_message": message,"message":"Please select branch for detail information","branch_list":branch_list})
   

def viewBranchDetail(request,branch_id):

    branch=get_object_or_404(Branch,pk=branch_id)

    student_list=Student.objects.filter(branch_id=branch_id)
    staff_list=Staff.objects.filter(branch_id=branch_id)
    course_list=Course.objects.filter(branch_id=branch_id)



    return render(request,"onboardportalapp/branchDetail.html",{"student_list":student_list, "staff_list":staff_list ,"branch_id":branch_id ,"course_list":course_list,"branch":branch })

def deleteBranch(request,branch_id):

    branch=get_object_or_404(Branch,pk=branch_id)
    branch.delete()
    branch_list=Branch.objects.all()
    return render(request,"onboardportalapp/branch.html",{"branch_list":branch_list})

def addStudentButton(request,branch_id):
    course=Course.objects.filter(branch_id=branch_id)
    return render(request,"onboardportalapp/student.html",{"message":"Fill the below form to add new student","branch_id":branch_id,"student":"","course_list":course})
def addStaffButton(request,branch_id):
    return render(request,"onboardportalapp/staff.html",{"message":"Fill the below form to add new staff","branch_id":branch_id,"staff":""})

def saveStudent(request):
     studentName=request.POST.get("student_name")
     start_date=request.POST.get("start_date")
     end_date=request.POST.get("end_date")
     course_name=request.POST.get("course_name")
     course=Course.objects.filter(pk=course_name)

     student=Student()
     branch_id=request.POST.get("branch_id")
     
     try:
        branch = Branch.objects.get(pk=branch_id)
     except Branch.DoesNotExist:
         # Handle the case where the branch does not exist
        branch = None
        
      
     student.student_name=studentName
     student.start_Date=start_date
     student.end_Date=end_date
     student.status=True
     student.branch=branch
     
   

     student.save()
     student.course.set(course)
     student.save()


     return redirect('onboard:viewBranchDetail',branch_id=branch_id)
     
def saveStaff(request):
    staff_name=request.POST.get("staff_name")
    experience=request.POST.get("experience")
    subject=request.POST.get("subject")
    branch_id=request.POST.get("branch_id")

    try:
       branch = Branch.objects.get(pk=branch_id)
    except Branch.DoesNotExist:
         # Handle the case where the branch does not exist
        branch = None

    staff=Staff()
    staff.staff_name=staff_name
    staff.experience=experience
    staff.status=True
    staff.subject=subject
    staff.branch=branch

    staff.save()

    student_list=Student.objects.filter(branch_id=branch_id)
    staff_list=Staff.objects.filter(branch_id=branch_id)
  

    return redirect('onboard:viewBranchDetail',branch_id=branch_id)



def editStudent(request,student_id):
    student=Student.objects.get(pk=student_id)
    print(student.start_Date,student.end_Date)
    course=Course.objects.all()
    course_student=student.course.all()

    branch_id=student.branch
 
    return render(request,"onboardportalapp/student.html",{"message":"Fill the below form to add new student","branch_id":student.branch,"student":student,"course_list":course,"course_student":course_student})

def deleteStudent(request,student_id):
    student=Student.objects.get(pk=student_id)
    branch_id=student.branch_id
    student.delete()
    return redirect('onboard:viewBranchDetail',branch_id=branch_id)


def saveUpdatedStudent(request,student_id):
     student=Student.objects.get(pk=student_id)
     studentName=request.POST.get("student_name")
     start_date=request.POST.get("start_date")
     end_date=request.POST.get("end_date")
     branch_id=request.POST.get("branch_id")
     course_name=request.POST.get("course_name")

     course=Course.objects.filter(id=course_name)

     try:
        branch = Branch.objects.get(pk=branch_id)
     except Branch.DoesNotExist:
         # Handle the case where the branch does not exist
        branch = None
        

     
     student.student_name=studentName
     student.start_Date=start_date
     student.end_Date=end_date
     student.status=True
     student.branch=branch
   

     student.save()
     student.course.set(course)

     student.save()
     student_list=Student.objects.filter(branch_id=branch_id)
     staff_list=Staff.objects.filter(branch_id=branch_id)
     course_list=Course.objects.filter(branch_id=branch_id)
     
     return render(request,"onboardportalapp/branchDetail.html",{"message":"Student Added","branch_id":branch_id,"student_list":student_list, "staff_list":staff_list,"course_list":course_list })


def editStaff(request,staff_id):
    staff=Staff.objects.get(pk=staff_id)

    return render(request,"onboardportalapp/staff.html",{"message":"Fill the below form to update  staff","branch_id":staff.branch,"staff":staff})

def deleteStaff(request,staff_id):
    staff=Staff.objects.get(pk=staff_id)
    branch_id=staff.branch.id
    staff.delete()
    return redirect('onboard:viewBranchDetail',branch_id=branch_id)

def saveUpdatedStaff(request,staff_id):
    staff=Staff.objects.get(pk=staff_id)
    staff_name=request.POST.get("staff_name")
    experience=request.POST.get("experience")
    subject=request.POST.get("subject")
    branch_id=request.POST.get("branch_id")

    try:
       branch = Branch.objects.get(pk=branch_id)
    except Branch.DoesNotExist:
         # Handle the case where the branch does not exist
        branch = None

    staff.staff_name=staff_name
    staff.experience=experience
    staff.status=True
    staff.subject=subject
    staff.branch=branch

    staff.save()
    

    return redirect("onboard:viewBranchDetail",branch_id=staff.branch.id)


def addCourseButton(request,branch_id):
    return render(request,"onboardportalapp/course.html",{"message":"Fill the below form to add new course","branch_id":branch_id})


def saveCourse(request):
    course_name=request.POST.get("course_name")
    course_duration=request.POST.get("course_duration")
    branch_id=request.POST.get("branch_id")

    try:
       branch = Branch.objects.get(pk=branch_id)
    except Branch.DoesNotExist:
         # Handle the case where the branch does not exist
        branch = None
 

 
    course=Course()
    course.course_name=course_name
    course.course_duration=course_duration
    course.branch=branch
    course.save()


    student_list=Student.objects.filter(branch_id=branch_id)
    staff_list=Staff.objects.filter(branch_id=branch_id)
    return redirect('onboard:viewBranchDetail',branch_id=branch_id)


def editCourse(request,course_id):
    course=Course.objects.get(pk=course_id)
    return render(request,"onboardportalapp/course.html",{"course":course})
  
def updateCourse(request,course_id):
     course=Course.objects.get(pk=course_id)

     course_name=request.POST.get("course_name")
     course_duration=request.POST.get("course_duration")
     branch_id=request.POST.get("branch_id")

     try:
       branch = Branch.objects.get(pk=branch_id)
     except Branch.DoesNotExist:
         # Handle the case where the branch does not exist
        branch = None
 

 
     course.course_name=course_name
     course.course_duration=course_duration
     course.branch=branch
     course.save()



     return redirect('onboard:viewBranchDetail',branch_id=branch_id)


def deleteCourse(request,course_id):
    course=Course.objects.get(pk=course_id)
    branch_id=course.branch_id
    course.delete()
    return redirect('onboard:viewBranchDetail',branch_id=branch_id)

