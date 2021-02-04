from django.urls import path

s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


from . import views

app_name = 'my_tests'

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.main_register,name = 'main_register'),
    path('accounts/login/',views.user_login,name = 'user_login'),
    path("<int:user_id>/o'quvchilar",views.search,name = 'search'),
    path('<int:user_id>/admin',views.admin,name = 'admin'),
    path('<int:user_id>/<int:admin_id>/admin',views.adminSettings,name = 'adminSettings'),
    path('<int:user_id>/<int:stud_id>/tahrirlash',views.edit,name = 'edit'),
    path('<int:user_id>/<int:stud_id>/saqlash',views.save,name = 'save'),
    path('<int:user_id>/<int:stud_id>/delete',views.delete,name = 'delete'),
    path('<int:user_id>/testlar',views.choice,name = 'choice'),
    path("<int:user_id>/<int:test_id>/test-qo'shis",views.add_test,name = 'add_test'),
    path('<int:user_id>/<int:test_id>/testni-tanlash',views.edit_test,name = 'edit_test'),
    path('<int:user_id>/<int:test_id>/edit-test-template/save',views.test_save,name = 'test_save'),
    path("<int:user_id>/<int:test_id>/<int:test_del>/testni-o'chirish",views.delete_test,name = 'delete_test'),
    path('<int:user_id>/<int:test_id>/testni-tahrirlash',views.edit_test_temp,name = 'edit_test_temp'),
    path('<int:user_id>/register/',views.register,name = 'register'),
    path('<int:user_id>/testlar/',views.tests,name = 'tests'),
    path('<int:user_id>/logout/',views.user_logout,name = 'user_logout'),
    path('<int:student_id>/test-tanlash/',views.student_choice,name = 'student_choice'),
    path('<int:stud_id>/profile/',views.user_profile,name = 'user_profile'),
    path('<int:student_id>/<int:test_id>/',views.test,name = 'test'),
    
]