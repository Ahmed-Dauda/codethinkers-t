from django.contrib import admin

# Register your models here.
# from users.models import NewUser
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('first_name','last_name','email', 'password','countries', 'phone_number','last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('first_name','last_name','email','countries','phone_number' ,'password1', 'password2')
            }
        ),
    )

    list_display = ('first_name','last_name', 'email','countries', 'phone_number','is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)
# admin.site.register(NewUser)