from django.contrib import admin
from .models import *


# Register your models here.

class LawyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Lawyer, LawyerAdmin)
