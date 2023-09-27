from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('taskview/<int:ids>/',views.task_view,name='taskview'),
    path('taskedit/<int:ids>',views.task_edit,name='taskedit'),
    path('taskdelete/<int:ids>',views.task_delete,name='taskdelete'),
    path('addtask',views.add_task,name='addtask'),
    path('usersignup',views.user_signup,name='usersignup'),
    path('login_view/',views.login_view,name='loginview'),
    path('logout_view/',views.logout_view,name='logoutview'),
    path('useredit/',views.useredit,name='useredit'),
    path('passwordchange/',views.password_charge,name='passwordchange'),
]

