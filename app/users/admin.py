from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.
class ProfileTabularInline(admin.TabularInline):
    model = Profile
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username']
    inlines = [
        ProfileTabularInline,
    ]

admin.site.register(CustomUser,CustomUserAdmin)
