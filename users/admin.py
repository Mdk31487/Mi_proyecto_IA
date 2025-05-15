from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass  # Aquí luego puedes personalizar el admin si deseas

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date')  # Puedes ajustar las columnas
