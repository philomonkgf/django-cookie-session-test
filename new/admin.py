from django.contrib import admin
from.models import Newuser,Task

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class NewuserAdmin(UserAdmin):
    list_display = ('email','username','is_staff','is_superuser',)
    readonly_fields = ('last_login','date_create','is_superuser','is_staff',)

    exclude = ()
    filter_horizontal = ()

    fieldsets = (None,{'fields':(
        'email','username','first_name','last_name','password','is_superuser','is_staff','last_login','date_create','bio',
        'user_permissions','groups',

    )}),
    
    add_fieldsets = (None,{'fields':(
        'email','username','first_name','last_name','bio','password1','password2',
    )}),













admin.site.register(Newuser,NewuserAdmin)
admin.site.register(Task)