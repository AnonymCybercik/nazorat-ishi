from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

import random

from django.urls import reverse

from django.contrib.auth import authenticate,logout,login
from my_tests.models import Student,Sinflarfanlar,Test

def register(request,user_id):

    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    school = request.POST.get('school')
    grade = request.POST.get('grade')
    password = request.POST.get('password')
    validator = request.POST.get('validator')
    viloyat = request.POST.get('viloyat')


    students = Student.objects.all()

    usernames = []    

    for student in students:
        usernames.append(student.username)
    

    full = ''

    if username and viloyat and password and first_name and last_name and school and grade and validator:
        if username in usernames:
            full = 'inusername'
        else:
            if password == validator:
                a = Student(first_name = first_name,last_name = last_name ,username = username , password = password,school=school,grade=grade,viloyat = viloyat)
                a.save()
                return HttpResponseRedirect(reverse("my_tests:register",args=(user_id,)))
            else:
                full = 'inpass'

    context = {

        "user_id":user_id,
        "error":full,

    }

    return render(request,'my_tests/register.html',context)

def admin(request,user_id):

    a = User.objects.get(id = user_id)

    all_students = Student.objects.all()
    all_tests = Test.objects.all()

    number_t = len(all_tests)
    number_s = len(all_students)

    context = {
        "user_id":a.id,
        "all_s":number_s,
        "all_t":number_t


    }

    return render(request,"my_tests/admin.html",context)

def user_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
        return HttpResponseRedirect(reverse("my_tests:admin",args=(user.id,)))
    
    context = {


    }

    return render(request,'my_tests/login.html',context)

def home(request):
    
    studensts = Student.objects.all()
    tests = Test.objects.all()

    context = {

        "studensts":len(studensts),
        "tests":len(tests)

    }

    return render(request,'my_tests/home.html',context)

def user_logout(request,user_id):
    logout(request)
    return HttpResponseRedirect(reverse("my_tests:user_login"))

def student_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    a = Student.objects.all()

    for i in a:
        if i.username == username:
            if i.password == password:
                return HttpResponseRedirect(reverse("my_tests:student_choice",args=(i.id,)))

    return render(request,'my_tests/student_login.html')

def choice(request,user_id):

    sinf = request.POST.get('sinf')
    fan = request.POST.get('fanlar')
     

    verificate =Sinflarfanlar.objects.all()

    for i in verificate:
        if i.sinf == sinf and i.fanlar == fan:
            a = Sinflarfanlar.objects.get(id = i.id)
            print('ready1')
            return HttpResponseRedirect(reverse('my_tests:add_test',args = (user_id,a.id,)))
           
    context = {
        'user_id':user_id
    }
    
    return render(request,'my_tests/choice.html',context)

def add_test(request,user_id,test_id):
    context = {

        "user_id":user_id,
        "test_id":test_id

    }

    A = request.POST.get('A')
    B = request.POST.get('B')
    C = request.POST.get('C')
    D = request.POST.get('D')
    question = request.POST.get('question')
    answer = request.POST.get('answer')

    tests = Sinflarfanlar.objects.get(id = test_id)

    if A and B and C and question and answer:
        tests.test_set.create(question = question,answer = answer, A = A, B = B,C = C,D=D)

    return render(request,'my_tests/add_test.html',context)

def student_choice(request,student_id):

    fan = request.POST.get('fanlar')
    sinf = request.POST.get('sinf')

    if fan and sinf:
        try:
            test = Sinflarfanlar.objects.get(fanlar = fan, sinf = sinf)
            return HttpResponseRedirect(reverse('my_tests:test',args=(student_id,test.id,)))
        except Exception as e:
            print(e)
    context = {
        'student_id':student_id
    }

    return render(request,'my_tests/student choice.html',context)

def test(request,student_id,test_id):

    t = 0

    testlar = Sinflarfanlar.objects.get(id = test_id)

    all_tests = testlar.test_set.order_by('?')[:30]

    for a in all_tests:
        data = request.POST.get(a.question)
        print(data,a.answer)
        if data == a.answer:
            t+=1
            return HttpResponse('to`g`ri javoblar: '+str(t))
    

    context = {
        'testlar':all_tests,
        'student_id':student_id,
        'test_id':test_id,
    }

    return render(request,'my_tests/test.html',context)

def search(request,user_id):

    grade = request.POST.get('grade')
    school = request.POST.get('school')
    viloyat = request.POST.get('viloyat')

    students = Student.objects.filter(grade = grade,school = school,viloyat = viloyat)

    context = {

        "students":students,
        "user_id":user_id

    }

    return render(request,"my_tests/students.html",context)

def generate(request,user_id):

    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$%&*_-'
    sr = ''.join(random.sample(s, len(s)))

    context = {

        "user_id":user_id,
        "recpas":sr[:10]

    }

    return render(request,'my_tests/register.html',context)
