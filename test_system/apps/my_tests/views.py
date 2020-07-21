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
                a.save()
                return HttpResponseRedirect(reverse("my_tests:register",args=(user_id,)))
            else:
                full = 'inpass'

    context = {

        "user_id":user_id,
        "error":full,
        "recpas":sr[:10]



    }

    return render(request,'my_tests/register.html',context)

def tests(request,user_id):
    a = User.objects.get(id = user_id)
    context = {
        "admin":a,
        'user_id':user_id,
    }
    return render(request,'my_tests/alls.html',context)




def admin(request,user_id):

    a = User.objects.get(id = user_id)

    all_students = Student.objects.all()
    all_tests = Test.objects.all()

    number_t = len(all_tests)
    number_s = len(all_students)

    context = {
        "user_id":a.id,
        "all_s":number_s,
        "all_t":number_t,
        "admin":a
    }

    return render(request,"my_tests/admin.html",context)
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
    
    
    

    return render(request,'my_tests/edit-admin.html',context)
def delete(request,user_id,stud_id):
    a = Student.objects.get(id = stud_id)
    a.delete()
    return HttpsResponseRedirect(reverse("my_tests:admin",args = (user_id,)))
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

    return HttpResponseRedirect(reverse("my_tests:edit",args=(user_id,stud_id,)))
def alls(request,user_id,test_id):

    a = Sinflarfanlar.objects.get(id = test_id)

    tests = a.test_set.order_by("-id")

    context = {
        "user_id":user_id,
        "tests":tests,
    }

    return render(request,"my_tests/alls.html",context)

def user_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    a = Student.objects.all()


    if user:
        return HttpResponseRedirect(reverse("my_tests:admin",args=(user.id,)))
    elif not(user):
        for i in a:
            if i.username == username:
                if i.password == password:
                    return HttpResponseRedirect(reverse("my_tests:student_choice",args=(i.id,)))
        for i in a:
            if i.username == username:
                if i.password == password:
                    if i.add_test == True:
                        return HttpResponseRedirect(reverse("my_tests:choice",args=(i.id,)))
        
    
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

    return render(request,"my_tests/students.html",context)
