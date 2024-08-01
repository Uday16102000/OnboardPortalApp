from django.urls import path
from . import views

app_name="onboard"
urlpatterns=[
    path("",views.landingPage, name="landingPage"),
    path("add-branch/",views.addBranch, name="addBranch"),
    path("<branch_id>/view-branch-details/",views.viewBranchDetail, name="viewBranchDetail"),
    path("<branch_id>/delete-branch/",views.deleteBranch, name="deleteBranch"),

    path("<branch_id>/add-stu/",views.addStudentButton,name="addStudentButton"),
    path("<branch_id>/add-sta/",views.addStaffButton,name="addStaffButton"),
    path("add-student/",views.saveStudent,name="saveStudent"),
    path("add-staff/",views.saveStaff,name="saveStaff"),
    path("<int:student_id>/edit-student/" ,views.editStudent, name="editStudent"),
    path("<int:student_id>/update-student/" ,views.saveUpdatedStudent, name="updateStudent"),
    path("<int:student_id>/delete-student/" ,views.deleteStudent, name="deleteStudent"),

       
    path("<int:staff_id>/edit-staff/" ,views.editStaff, name="editStaff"),
    path("<int:staff_id>/delete-staff/" ,views.deleteStaff, name="deleteStaff"),
    path("<int:staff_id>/update-staff/" ,views.saveUpdatedStaff, name="updateStaff"),

    path("<branch_id>/add-br",views.addCourseButton,name="addCourseButton"),
    path("save-course/",views.saveCourse, name="saveCourse"),
    path("<course_id>/edit-course",views.editCourse,name="editCourse"),
    path("<course_id>/update-course",views.updateCourse,name="updateCourse"),
    path("<course_id>/delete-course/",views.deleteCourse,name="deleteCourse"),

    path("signIn/",views.signIn,name="signIn")
]