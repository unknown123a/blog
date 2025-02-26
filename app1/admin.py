from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,home
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # Optional: Use a custom form if needed

    # Display and permissions in admin
    list_display = ['email', 'name', 'is_staff', 'is_active']
    search_fields = ('email', 'name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'name', 'password1', 'password2','avatar')}),
    )

# Register the custom user and admin
admin.site.register(home)
admin.site.register(CustomUser, CustomUserAdmin)
