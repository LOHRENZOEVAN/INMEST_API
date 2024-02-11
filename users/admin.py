
# Register your models here.
# admin.py

from django.contrib import admin
from .models import IMUser, Cohort, CohortMember

@admin.register(IMUser)
class IMUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'is_active', 'date_created')

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'year', 'start_date', 'end_date', 'is_active', 'date_created', 'date_modified', 'author')

@admin.register(CohortMember)
class CohortMemberAdmin(admin.ModelAdmin):
    list_display = ('cohort', 'member', 'is_active', 'date_created', 'date_modified', 'author')

