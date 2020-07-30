from django.urls import path

from . import views

app_name = 'my_tests'

urlpatterns = [
    path('',views.user_login,name = 'user_login'),
    path('\d{<int:user_id>}/students',views.search,name = 'search'),
    path('\d{<int:user_id>}/admin',views.admin,name = 'admin'),
    path('\d{<int:user_id>}/\d{<int:stud_id>}/edit',views.edit,name = 'edit'),
    path('\d{<int:user_id>}/\d{<int:stud_id>}/save',views.save,name = 'save'),
    path('\d{<int:user_id>}/\d{<int:stud_id>}/delete',views.delete,name = 'delete'),
    path('\d{<int:user_id>}/choice',views.choice,name = 'choice'),
    path('\d{<int:user_id>}/\d{<int:test_id>}/add-test',views.add_test,name = 'add_test'),
    path('\d{<int:user_id>}/\d{<int:test_id>}/edit-test',views.edit_test,name = 'edit_test'),
    path('\d{<int:user_id>}/register/',views.register,name = 'register'),
    path('\d{<int:user_id>}/tests/',views.tests,name = 'tests'),
    path('\d{<int:user_id>}/logout/',views.user_logout,name = 'user_logout'),
    path('\d{<int:student_id>}/choice/',views.student_choice,name = 'student_choice'),
    path('\d{<int:student_id>}/\d{<int:test_id>}/',views.test,name = 'test'),
    
]