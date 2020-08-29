from django.urls import path

s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


from . import views

app_name = 'my_tests'

urlpatterns = [
    path(r'accounts/login/',views.user_login,name = 'user_login'),
    path(r'<int:user_id>/students',views.search,name = 'search'),
    path(r'<int:user_id>/admin',views.admin,name = 'admin'),
    path(r'<int:user_id>/<int:admin_id>/admin',views.adminSettings,name = 'adminSettings'),
    path(r'<int:user_id>/<int:stud_id>/edit',views.edit,name = 'edit'),
    path(r'<int:user_id>/<int:stud_id>/save',views.save,name = 'save'),
    path(r'<int:user_id>/<int:stud_id>/delete',views.delete,name = 'delete'),
    path(r'<int:user_id>/choice',views.choice,name = 'choice'),
    path(r'<int:user_id>/<int:test_id>/add-test',views.add_test,name = 'add_test'),
    path(r'<int:user_id>/<int:test_id>/edit-test',views.edit_test,name = 'edit_test'),
    path(r'<int:user_id>/<int:test_id>/edit-test-template/save',views.test_save,name = 'test_save'),
    path(r'<int:user_id>/<int:test_id>/<int:test_del>/edit-test-template/delete',views.delete_test,name = 'delete_test'),
    path(r'<int:user_id>/<int:test_id>/edit-test-template',views.edit_test_temp,name = 'edit_test_temp'),
    path(r'<int:user_id>/register/',views.register,name = 'register'),
    path(r'<int:user_id>/tests/',views.tests,name = 'tests'),
    path(r'<int:user_id>/logout/',views.user_logout,name = 'user_logout'),
    path(r'<int:student_id>/choice/',views.student_choice,name = 'student_choice'),
    path(r'<int:stud_id>/profile/',views.user_profile,name = 'user_profile'),
    path(r'<int:student_id>/<int:test_id>/',views.test,name = 'test'),

]
