from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

class UserAdmin(BaseUserAdmin):
    # Define which fields should be displayed in the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'otp_secret_key', 'is_staff')

    # Define the fieldsets to be shown on the change user admin page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define the add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

# Register the custom UserAdmin
admin.site.register(User, UserAdmin)

# Since we're using a custom User model, unregister the Group model
# admin.site.unregister(Group)
