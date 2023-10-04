from django import forms
from .models import Task,Newuser

from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskname','taskimage','abouttask',]

        

class signup_form(UserCreationForm):
    class Meta:
        model = Newuser
        fields = ['username','email','name','first_name','last_name','bio']



class user_edit(UserChangeForm):
    password = None
    
    class Meta:
        model = Newuser
        fields = ['email','username','name','first_name','last_name','bio',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].disabled = True

