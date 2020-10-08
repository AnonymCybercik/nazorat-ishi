from django import forms
from django.contrib.auth.forms import UserCreationForm

from my_tests.models import Student


class CreateUserForm(UserCreationForm):

    viloyatlar = (
        ("Jizzax shaxar"   , "Jizzax shaxar"),
        ("Arnasoy"		   , "Arnasoy tumani"),
        ("Baxmal"		   , "Baxmal tumani"),
        ("Sharof Rashidov" , "Sharof Rashidov tumani"),
        ("Zarbdor"		   , "Zarbdor tumani"),
        ("Zafarobod"	   , "Zafarobod tumani"),
        ("Zomin"		   , "Zomin tumani"),
        ("Zomin"		   , "Zomin tumani"),
        ("Mirzacho'l"	   , "Mirzacho`l tumani"),
        ("Paxtakor"		   , "Paxtakor tumani"),
        ("Yangiobod"	   , "Yangiobod tumani"),
        ("Forish"		   , "Forish tumani"),
        ("G'allaorol"	   , "G`allaorol tumani"),
        )

    grade1 = (
        ("9","9"),
        ("10","10"),
        ("11","11"),
        )
    grade2 = (
        ("A","A"),
        ("B","B"),
        ("V","V"),
        ("G","G"),
        ("D","D"),
        )

    username =      forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'form-input','autocomplete': 'off','placeholder':'Username'}))
    first_name =    forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'form-input','autocomplete': 'off','style':"width: 50%; display:inline-block;",'placeholder':'Ism'}))
    last_name =     forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'form-input','autocomplete': 'off','style':"width: 49%; display:inline-block;",'placeholder':'Familya'}))
    viloyat =       forms.ChoiceField(required = True,widget=forms.Select(attrs={'class': 'form-input'}),choices = viloyatlar)
    grade =         forms.ChoiceField(required = True,choices = grade1,widget=forms.Select(attrs={'class': 'form-input student','style':"width: 50%;",'id':"requirment3"}))
    grade2 =        forms.ChoiceField(required = True,choices = grade2,widget=forms.Select(attrs={'class': 'form-input student','style':"width: 49%;",'id':"requirment2"}))
    school =        forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'form-input student','autocomplete': 'off','placeholder':'Maktab raqami','id':"requirment"}))
    password1 =     forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'form-input','type':'password','placeholder':'Foydalanuvchi Paroli'}))
    password2 =     forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'form-input','type':'password','placeholder':'Parolni qayta kiriting'}))


