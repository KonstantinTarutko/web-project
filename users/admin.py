from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User


admin.site.register(User)


# admin.site.register(User, CustomUserAdmin)   for other django admin
