from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random

from django.urls import reverse

from django.contrib.auth import authenticate,logout,login
from my_tests.models import Student,Sinflarfanlar,Test,AdditionalAdmin
from my_tests.decorators import allowed_users,unauthenticated_user


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles = ['admin2'])
def home(request,user_id):
    return render(request,"my_tests/admin/home.html",{"user_id":user_id})

@login_required(login_url='/accounts/login/')
def register(request,user_id):

    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    school = request.POST.get('school')
    grade = request.POST.get('grade')
    grade2 = request.POST.get('grade2')
    password = request.POST.get('password')
    validator = request.POST.get('validator')
    viloyat = request.POST.get('viloyat')


    students = Student.objects.all()

    data = username,first_name,last_name,school,grade,password,validator,viloyat


    usernames = []

    for student in students:
        usernames.append(student.username)


    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$%&*_-'
    sr = ''.join(random.sample(s, len(s)))

    full = ''

    if username and viloyat and password and first_name and last_name and school and grade and validator:
        if username in usernames:
            full = 'inusername'
        else:
            if password == validator:
                a = Student(first_name = first_name,last_name = last_name ,username = username , password = password,school=school,grade=grade,grade2=grade2,viloyat = viloyat)
                n = User(username = username , password = password)
                n,a.save()
                return redirect(reverse("admin_my_tests:register",args=(user_id,)))
            else:
                full = 'inpass'


    context = {

        "user_id":user_id,
        "error":full,
        "recpas":sr[:10]



    }


    return render(request,"my_tests/admin/register.html",context)


@login_required(login_url='/accounts/login/')
def edit_test(request,user_id,test_id):

    test = Sinflarfanlar.objects.get(id = test_id)
    test = test.test_set.order_by("id")

    context = {
        "user_id":   user_id,
        "test_id":   test_id,
        "test":      test,
    }


    return render(request,"my_tests/admin/edit-test.html",context)

@login_required(login_url='/accounts/login/')
def delete(request,user_id,stud_id):
    try:
        a = Student.objects.get(id = stud_id)
        a.delete()
    except:
        return redirect(reverse("admin_my_tests:search",args = (user_id,)))

    return redirect(reverse("admin_my_tests:search",args = (user_id,)))

@login_required(login_url='/accounts/login/')
def save(request,user_id,stud_id):
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    school = request.POST.get('school')
    grade = request.POST.get('grade')
    grade2 = request.POST.get('grade2')
    password = request.POST.get('password')
    viloyat = request.POST.get('viloyat')
    validator = request.POST.get('validator')

    n = []

    a = Student.objects.get(id = stud_id)
    alls = Student.objects.all()
    for d in alls:
        n.append(d)

    if not(username in alls):
        a.username =   str(username)


    if password != a.password and (password == validator):a.password = str(password);

    a.first_name = str(first_name)
    a.last_name =  str(last_name)
    a.school  =    str(school)
    a.grade  =     str(grade)
    a.grade2  =    str(grade2)
    a.viloyat  =   str(viloyat)
    a.save()

    return redirect("admin_my_tests:edit",args=(user_id,stud_id,))

@login_required(login_url='/accounts/login/')
def user_logout(request,user_id):
    logout(request)
    return redirect('my_tests:user_login')

@login_required(login_url='/accounts/login/')
def choice(request,user_id):

    verificate9 =Sinflarfanlar.objects.all().filter(sinf='9')
    verificate10 =Sinflarfanlar.objects.all().filter(sinf='10')
    verificate11 =Sinflarfanlar.objects.all().filter(sinf='11')



    context = {
        'user_id':user_id,
        "verificate9":verificate9,
        "verificate10":verificate10,
        "verificate11":verificate11,
    }

    return render(request,"my_tests/admin/adminChoise.html",context)

@login_required(login_url='/accounts/login/')
def add_test(request,user_id,test_id):



    A = request.POST.get('A')
    B = request.POST.get('B')
    C = request.POST.get('C')
    D = request.POST.get('D')

    question = request.POST.get('question')
    answer = request.POST.get('answer')

    tests = Sinflarfanlar.objects.get(id = test_id)

    if A and B and C and question and answer:
        tests.test_set.create(question = question,answer = answer, A = A, B = B,C = C,D=D)

    context = {

        "user_id":user_id,
        "test_id":test_id,

    }


    return render(request,"my_tests/admin/add_test.html",context)



@login_required(login_url='/accounts/login/')
def search(request,user_id):


    grade = request.POST.get('grade')
    grade2 = request.POST.get('grade2')
    school_data = request.POST.get('school')
    viloyat = request.POST.get('viloyat')
    students = Student.objects.filter(grade = grade,grade2 = grade2,school = school_data,viloyat = viloyat).order_by('last_name')


    context = {

        "students":students,
        "grade":grade,
        "user_id":user_id,
        "school_data":school_data,
        "viloyat":viloyat,
    }
    return render(request,"my_tests/admin/students.html",context)

@login_required(login_url='/accounts/login/')
def edit(request,user_id,stud_id):

    a = Student.objects.get(id = stud_id)

    context = {
        "user_id":   user_id,
        "stud_id":   stud_id,
        "username":  a.username,
        "first_name":a.first_name,
        "last_name": a.last_name,
        "school":    a.school,
        "grade":     a.grade,
        "grade2":    a.grade2,
        "password":  a.password,
        "viloyat":   a.viloyat,
    }

    return render(request,"my_tests/admin/edit-stud.html",context)

@login_required(login_url='/accounts/login/')
def edit_test_temp(request,user_id,test_id):

    a = Test.objects.get(id = test_id)

    context = {
        "user_id":user_id,
        "test_id":test_id,
        "question":a.question,
        "A":a.A,
        "B":a.B,
        "C":a.C,
        "D":a.D,
        "answer":a.answer,
    }

    return render(request,"my_tests/admin/add_test_temp.html",context)

@login_required(login_url='/accounts/login/')
def test_save(request,user_id,test_id):

    question = request.POST.get('question')
    A = request.POST.get('A')
    B = request.POST.get('B')
    C = request.POST.get('C')
    D = request.POST.get('D')
    answer = request.POST.get('answer')

    a = Test.objects.get(id = test_id)

    if A and B and C and question and answer:
        a.question = question
        a.A = A
        a.B = B
        a.C = C
        a.D = D
        a.answer = answer
        a.save()


        return redirect(reverse("admin_my_tests:edit_test_temp",args=(user_id,test_id,)))

@login_required(login_url='/accounts/login/')
def delete_test(request,user_id,test_id,test_del):
    try:
        a = Test.objects.get(id = test_del)
        a.delete()
    except:
        return redirect(reverse("admin_my_tests:edit_test",args = (user_id,test_id)))


    return redirect(reverse("admin_my_tests:edit_test",args = (user_id,test_id)))