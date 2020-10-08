from django.urls import path
import random

s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


from . import adminviews
from . import views

app_name = 'admin_my_tests'

urlpatterns = [
    path(r'accounts/login',views.user_login,name='user_login'),
    path(r'<int:user_id>/home',adminviews.home,name = 'home'),
    path(r'<int:user_id>/students',adminviews.search,name = 'search'),
    path(r'<int:user_id>/{<int:stud_id>/edit',adminviews.edit,name = 'edit'),
    path(r'<int:user_id>/{<int:stud_id>/save',adminviews.save,name = 'save'),
    path(r'<int:user_id>/{<int:stud_id>/delete',adminviews.delete,name = 'delete'),
    path(r'<int:user_id>/choice',adminviews.choice,name = 'choice'),
    path(r'<int:user_id>/{<int:test_id>/add-test',adminviews.add_test,name = 'add_test'),
    path(r'<int:user_id>/{<int:test_id>/edit-test',adminviews.edit_test,name = 'edit_test'),
    path(r'<int:user_id>/{<int:test_id>/edit-test-template/save',adminviews.test_save,name = 'test_save'),
    path(r'<int:user_id>/{<int:test_id>/<int:test_del>/edit-test-template/delete',adminviews.delete_test,name = 'delete_test'),
    path(r'<int:user_id>/{<int:test_id>/edit-test-template',adminviews.edit_test_temp,name = 'edit_test_temp'),
    path(r'<int:user_id>/register/',adminviews.register,name = 'register'),
    path(r'<int:user_id>/logout/',adminviews.user_logout,name = 'user_logout'),

]
