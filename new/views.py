from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q


from .models import Task
from.forms import Taskform,signup_form,user_edit

# Create your views here.


@login_required(login_url='loginview')
def index(request):
    q = request.GET.get('q')
    if q:
        tasks = Task.objects.filter(Q(taskname__contains=q)|Q(taskname__icontains=q))
    else:
        tasks = Task.objects.all().order_by('-taskcreate')
    request.session['sname'] = request.user.email
    reponse = render(request,'new/index.html',{'tasks':tasks})
    reponse.set_cookie('name',request.user.name)
    return reponse


@login_required(login_url='loginview')
def task_view(request,ids):
    taskview = Task.objects.get(pk=ids)
    name = request.COOKIES.get('name')
    sess=request.session['sname']
    return render(request,'new/taskview.html',{'task':taskview,'name':name,'sess':sess})

@login_required(login_url='loginview')
def task_edit(request,ids):
    task = Task.objects.get(pk=ids)
    taskform = Taskform(instance=task)
    if request.method =="POST":
        form = Taskform(request.POST,request.FILES,instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('index')
    return render(request,'new/edittask.html',{'form':taskform})

@login_required(login_url='loginview')
def task_delete(request,ids):
    task = Task.objects.get(pk=ids)
    task.delete()
    return redirect ('index')


@login_required(login_url='loginview')
def add_task(request):
    form = Taskform()
    if request.method =='POST':
        form = Taskform(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.taskusername = request.user
            user.save()
            return redirect('index')
    return render(request,'new/addtask.html',{'form':form})


def user_signup(request):
    if request.method == "POST":
        user = signup_form(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            return redirect('index')
        else:
            return render(request,'new/signup.html',{'form':user})
    return render(request,'new/signup.html',{'form':signup_form()})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'new/login.html',{'message':'invalid credentials'})

    return render(request,'new/login.html')



def logout_view(request):
    logout(request)
    return redirect('loginview')



def useredit(request):
    form = user_edit(instance = request.user)
    if request.method == "POST":
        form = user_edit(request.POST,request.FILES,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'new/useredit.html',{'form':form})
    return render(request,'new/useredit.html',{'form':form})


def password_charge(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'new/passwordchage.html',{'form':form})
        
    return render(request,'new/passwordchage.html',{'form':PasswordChangeForm(user = request.user)})









