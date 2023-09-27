# Generated by Django 4.2.5 on 2023-09-25 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=24)),
                ('taskimage', models.ImageField(upload_to='')),
                ('abouttask', models.TextField()),
                ('taskcreate', models.DateTimeField(auto_now=True)),
                ('taskedit', models.DateTimeField(auto_now_add=True)),
                ('taskusername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
