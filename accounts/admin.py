from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "birthday",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("birthday",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("birthday",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
