from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'role',
                'profile_picture',
                'bio',
                'date_of_birth',
                'enrollment_date',
                'phone_number',
                'address',
                'linkedin_profile',
                'skills',
            )
        }),
    )

admin.site.register(User, CustomUserAdmin)
