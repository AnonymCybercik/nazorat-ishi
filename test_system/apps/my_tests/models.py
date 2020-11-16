from django.db import models


class Student(models.Model):
    viloyat = models.CharField(max_length=20,null=True)
    school = models.CharField(max_length=20,null=True)
    grade = models.CharField(max_length=20,null=True)
    grade2 = models.CharField(max_length=20,null=True)
    username = models.CharField(max_length=20,null=True)
    is_student = models.BooleanField(null=True)
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)

class Sinflarfanlar(models.Model):
    sinf = models.CharField(max_length = 2,choices=[
        ('9','9'),
        ('10','10'),
        ('11','11')
    ],null=True)
    fanlar = models.CharField(max_length=30,choices= [
        ('Ona tili', 'Ona tili'),
        ('Adabiyot','Adabiyot'),
        ('Fizika','Fizika'),
        ('Algebra','Algebra'),
        ('Rus tili','Rus tili'),
        ('Kimyo','Kimyo'),
        ('Biologiya','Biologiya'),
        ('Informatika','Informatika'),
        ('Ingliz tili','Ingliz tili'),
        ('Geometriya','Geometriya'),
        ('Huquq','Huquq'),
        ('Tarix','Tarix'),
    ],null = True)

class Test(models.Model):
    test = models.ForeignKey(Sinflarfanlar,on_delete=models.CASCADE)
    question = models.CharField(max_length=160,null = True)
    A = models.CharField(max_length=60,null=True)
    B = models.CharField(max_length=60,null=True)
    C = models.CharField(max_length=60,null=True)
    D = models.CharField(max_length=60,null=True)
    answer = models.CharField(max_length=60,null=True)
    number = models.CharField(max_length = 2,null = True)

class AdditionalAdmin(models.Model):
    username = models.CharField(max_length = 20,null = True)
    password = models.TextField(null = True)

    allow    = models.BooleanField(null = True)
