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

    username =      forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'input','style':"width: 45%; display:inline-block;",'autocomplete': 'off'}))
    first_name =    forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'input','autocomplete': 'off','style':"width: 45%; display:inline-block;"}))
    last_name =     forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'input','autocomplete': 'off','style':"width: 45%; display:inline-block;"}))
    viloyat =       forms.ChoiceField(required = True,widget=forms.Select(attrs={'class': 'select3'}),choices = viloyatlar)
    grade =         forms.ChoiceField(required = True,choices = grade1,widget=forms.Select(attrs={'class': 'select1','style':"width: 45%; display:inline-block;"}))
    grade2 =        forms.ChoiceField(required = True,choices = grade2,widget=forms.Select(attrs={'class': 'select2','style':"width: 45%; display:inline-block;"}))
    school =        forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'input','style':"width: 45%; display:inline-block;",'autocomplete': 'off',}))
    password1 =     forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'input','type':'password',}))
    password2 =     forms.CharField(required = True,max_length = 75,widget=forms.TextInput(attrs={'class': 'input','type':'password',}))


