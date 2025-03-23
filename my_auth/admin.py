from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    UserProfile
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    ordering = ('id',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'saved_recipes')}),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'vegetarian')
    search_fields = ('user__username',)
    list_filter = ('vegetarian',)


