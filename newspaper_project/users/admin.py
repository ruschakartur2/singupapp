from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','surname','age','profile_image','is_staff','date_joined']


admin.site.register(CustomUser, CustomUserAdmin)
