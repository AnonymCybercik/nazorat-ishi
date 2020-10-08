from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from my_tests.forms import CreateUserForm
from my_tests.decorators import allowed_users,unauthenticated_user

import random

from django.urls import reverse
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate,logout,login
from my_tests.models import Student,Sinflarfanlar,Test,AdditionalAdmin

def home(request):

    a = request.user
    fanlar = Sinflarfanlar.objects.all()
    students = Student.objects.all()
    testlar = Test.objects.all()

    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    if group == 'admin2':
        admin2 = True
    else:
        admin2 = False

    if group == 'admin':
        admin = True
    else:
        admin = False
    if group == 'student':
        student = True
    else:
        student = False

    if a:
        user = True
    else:
        user = False

    context = {

        "user":a,
        "fanlar":len(fanlar),
        "students":len(students),
        "testlar":len(testlar),
        "admin":admin,
        "admin2":admin2,
        "student":student,

        }

    return render(request,'my_tests/home.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def register(request,user_id):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            school = form.cleaned_data.get('school')
            grade = form.cleaned_data.get('grade')
            grade2 = form.cleaned_data.get('grade2')
            viloyat = form.cleaned_data.get('viloyat')
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)

            a = Student(first_name = first_name,last_name = last_name ,username = username , password = password,school=school,grade=grade,grade2=grade2,viloyat = viloyat)
            a.save()
            return redirect(reverse("my_tests:register",args = (user_id,)))





    context = {


        'user_id':user_id,
        'form':form


    }

    return render(request,'my_tests/register.html',context)
def main_register(request):
    form = CreateUserForm()

    is_student = request.POST.get('is_student')




    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            school = form.cleaned_data.get('school')
            grade = form.cleaned_data.get('grade')
            grade2 = form.cleaned_data.get('grade2')
            viloyat = form.cleaned_data.get('viloyat')
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)




            a = Student(first_name = first_name,last_name = last_name ,is_student = is_student,username = username , password = password,school=school,grade=grade,grade2=grade2,viloyat = viloyat)
            a.save()
            return redirect(reverse("my_tests:user_login"))





    context = {

        'form':form


    }

    return render(request,'my_tests/main_register.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def admin(request,user_id):

    a = User.objects.get(id = user_id)
    n = AdditionalAdmin.objects.get(id = 1)

    all_students = Student.objects.all()
    all_tests = Test.objects.all()

    number_t = len(all_tests)
    number_s = len(all_students)

    context = {
        "user_id":a.id,
        "all_s":number_s,
        "all_t":number_t,
        "admin":a,
        "admins":n
    }

    return render(request,"my_tests/admin.html",context)
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def edit_test(request,user_id,test_id):

    test = Sinflarfanlar.objects.get(id = test_id)
    test = test.test_set.order_by("id")

    context = {
        "user_id":   user_id,
        "test_id":   test_id,
        "test":      test,
    }





    return render(request,'my_tests/edit-test.html',context)
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def delete(request,user_id,stud_id):
    try:
        a = Student.objects.get(id = stud_id)
        user = authenticate(username = a.username,password = a.password)
        user.delete()
        a.delete()
    except:
        return redirect(reverse("my_tests:search",args = (user_id,)))

    return redirect(reverse("my_tests:search",args = (user_id,)))


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
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

    user = authenticate(username = a.username,password = a.password)

    w = User.objects.get(id = user.id)

    alls = Student.objects.all()
    for d in alls:
        n.append(d)

    if not(username in alls):
        a.username =   str(username)

    if (password == validator):
        a.password = str(password)

    a.first_name = str(first_name)
    a.last_name =  str(last_name)
    a.school  =    str(school)
    a.grade  =     str(grade)
    a.grade2  =    str(grade2)
    a.viloyat  =   str(viloyat)
    a.save()

    w.username = a.username
    w.password = a.password
    w.save()


    return redirect(reverse("my_tests:edit",args=(user_id,stud_id,)))


def user_login(request):

    username = request.POST.get('username')
    password =request.POST.get('password')

    user = authenticate(username=username, password=password)
    if request.method == "POST":
        if user is not None:
            login(request, user)

            return redirect(reverse("my_tests:home"))


        else:
            messages.info(request,'Username yoki Parolda xatolik bor')
            return redirect(reverse("my_tests:user_login"))

    context = {}
    return render(request, 'my_tests/login.html', context)



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['student'])
def user_profile(request,stud_id):

    b = User.objects.get(id = stud_id)
    a = Student.objects.get(username = b.username)

    context = {
        "stud_id":stud_id,
        "student":a,
    }

    return render(request,'my_tests/user-profile.html',context)


@login_required(login_url='/accounts/login/')
def user_logout(request,user_id):
    logout(request)
    return redirect("my_tests:user_login")

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
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

    return render(request,'my_tests/choice.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
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

    return render(request,'my_tests/add_test.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['student'])
def student_choice(request,student_id):

    verificate9 =Sinflarfanlar.objects.all().filter(sinf='9')
    verificate10 =Sinflarfanlar.objects.all().filter(sinf='10')
    verificate11 =Sinflarfanlar.objects.all().filter(sinf='11')


    context = {
        'student_id':student_id,
        "verificate9":verificate9,
        "verificate10":verificate10,
        "verificate11":verificate11,
    }

    return render(request,'my_tests/student choice.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def adminSettings(request,user_id,admin_id):

    n = AdditionalAdmin.objects.get(id = admin_id)

    allow = request.POST.get("admin")

    if allow == True:
        n.allow = True
        n.save()
    else:
        n.allow = False
        n.save()



    return redirect(reverse("my_tests:admin",args = (user_id,)))

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['student'])
def test(request,student_id,test_id):

    t = 0

    testlar = Sinflarfanlar.objects.get(id = test_id)
    data = request.POST
    all_tests = testlar.test_set.order_by('?')[:30]
    if data:
        for a in all_tests:
            data = request.POST.get(a.question)
            if data == a.answer:
                t+=1


        return render(request,'my_tests/result.html',{"javob":t,"student_id":student_id})



    context = {
        'testlar':all_tests,
        "test_name":testlar,
        'student_id':student_id,
        'test_id':test_id,
    }

    return render(request,'my_tests/test.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def search(request,user_id):


    grade = request.GET.get('grade')
    grade2 = request.GET.get('grade2')
    school_data = request.GET.get('school')
    viloyat = request.GET.get('viloyat')

    students = Student.objects.filter(grade = grade,grade2 = grade2,school = school_data,viloyat = viloyat).order_by('last_name')


    context = {

        "students":students,
        "grade":grade,
        "user_id":user_id,
        "school_data":school_data,
        "viloyat":viloyat,
    }

    return render(request,"my_tests/students.html",context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def edit(request,user_id,stud_id):

    a = Student.objects.get(id = stud_id)
    form = CreateUserForm()
    if request.method == 'GET':
        form.first_name = 'salom'

    context = {
        "user_id":   user_id,
        "stud_id":   stud_id,
        "username":  a.username,
        "first_name":a.first_name,
        "last_name": a.last_name,
        "school":    a.school,
        "password":  a.password,
        "grade":     a.grade,
        "grade2":    a.grade2,
        "password":  a.password,
        "viloyat":   a.viloyat,
        "form":form,
    }


    return render(request,'my_tests/edit-stud.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
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

    return render(request,'my_tests/add_test_temp.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
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


        return redirect(reverse("my_tests:edit_test_temp",args=(user_id,test_id,)))

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def delete_test(request,user_id,test_id,test_del):
    try:
        a = Test.objects.get(id = test_del)
        a.delete()
    except:
        return redirect(reverse("my_tests:edit_test",args = (user_id,test_id)))


    return redirect(reverse("my_tests:edit_test",args = (user_id,test_id)))

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin'])
def tests(request,user_id):
    a = User.objects.get(id = user_id)
    context = {
        "admin":a,
        'user_id':user_id,
    }
    return render(request,'my_tests/alls.html',context)


    return redirect(reverse("my_tests:edit_test",args = (user_id,test_id)))


def views_404(request):
    return render(request,'my_tests/404.html')

