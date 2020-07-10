from django.urls import path

from . import views

app_name = 'my_tests'

urlpatterns = [
    path('',views.user_login,name = 'user_login'),
    path('<int:user_id>/students',views.search,name = 'search'),
    path('<int:user_id>/regsiter',views.generate,name = 'generate'),
    path('<int:user_id>/admin',views.admin,name = 'admin'),
    path('<int:user_id>/add-admin',views.add_admin,name = 'add_admin'),
    path('<int:user_id>/edit-admin',views.edit_admin,name = 'edit_admin'),
    path('<int:user_id>/choice',views.choice,name = 'choice'),
    path('<int:user_id>/<int:test_id>/add-test',views.add_test,name = 'add_test'),
    path('<int:user_id>/register/',views.register,name = 'register'),
    path('<int:user_id>/logout/',views.user_logout,name = 'user_logout'),
    path('<int:student_id>/choice/',views.student_choice,name = 'student_choice'),
    path('<int:student_id>/<int:test_id>/',views.test,name = 'test'),
    
]