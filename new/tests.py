from django.test import TestCase,Client
from.models import Newuser,Task

from django.urls import reverse


# Create your tests here.


#TESTING MODEL 

class Test_model_user(TestCase):
    def test_user_model(self):
        email = 'test@gmail.com'
        username = 'aaaname'
        password = 'Hello@world'

        user = Newuser.objects.create_user(
            email=email,username=username,password=password
        )


        self.assertEqual(user.email,email)
        self.assertEqual(user.username,username)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)



    def test_superuser_model(self):
        email = 'test@gmail.com'
        username = 'aaaname'
        password = 'Hello@world'

        user = Newuser.objects.create_superuser(
            username=username,password=password,email=email
        )

        self.assertEqual(user.email,email)
        self.assertEqual(user.username,username)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)



class Test_view(TestCase):
    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.taskview = reverse('taskview',args=[1])
        self.loginview = reverse('loginview')
        self.addtaskview = reverse('addtask')

    def test_index_view(self):
        response = self.client.get(self.index)

        self.assertEqual(response.status_code,302)   #-------->302 redircts login  page
        
        # self.assertTemplateUsed(response,'new/index.html')

    def test_taskview(self):
        response = self.client.get(self.taskview)
        self.assertEqual(response.status_code,302)


    def test_login_view(self):
        user = Newuser.objects.create_user(email='testuser@gmail.com',password='12345',username='aaa')
        
        login = self.client.login(email='testuser@gmail.com',password= '12345')
        response = self.client.get(self.loginview)

        self.assertTrue(login)
        self.assertEqual(response.status_code,200)
        # self.assertEquals(response.status_code, 401)


    def test_add_task(self):
       
        user = Newuser.objects.create_user(email='testuser@gmail.com',password='12345',username='aaa')
        task = Task.objects.create(
            taskusername=user,taskname='wwww',abouttask='aboutask'
        )

        response = self.client.post(self.addtaskview,{
            'taskusername':user,
            'taskname':'wwww',
            'abouttask':'aboutask',

        })

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'new/addtask.html')
        self.assertContains(response,'taskname')
        self.assertEqual(Task.objects.count(),1)




        




















