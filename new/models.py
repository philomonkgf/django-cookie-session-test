from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


#signals
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,post_delete



# Create your models here.
class Makeuser(BaseUserManager):
    def create_user(self,username,email,password,*args,**kwargs):
        if not username:
            raise ValueError('user should have username')
        if not email:
            raise ValueError('user should have email')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email)

        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,username,email,password,*args,**kwargs):
        user = self.create_user(
            username=username,
            email = email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
    


class Newuser(AbstractBaseUser,PermissionsMixin):
    username  = models.CharField(max_length=24)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    bio = models.ImageField()
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = Makeuser()



class Task(models.Model):
    taskusername = models.ForeignKey(Newuser,on_delete=models.CASCADE)
    taskname = models.CharField(max_length=24)
    taskimage = models.ImageField()
    abouttask = models.TextField()
    taskcreate = models.DateTimeField(auto_now=True)
    taskedit = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.taskname}'
    

#after save
@receiver(post_save,sender=Task)
def user_task_created(sender,instance,created,*aggs,**kwargs):
    if created:
        print('task as be create')
    else:
        print('erorr in task')



#after delete
@receiver(post_delete,sender=Task)
def user_task_created(sender,instance,*aggs,**kwargs):
    if instance:
        print('task as be delete')
    else:
        print('erorr in task delete')








