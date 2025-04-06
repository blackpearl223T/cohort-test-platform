from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Cohort, CohortMembership

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_teacher', 'is_staff')
    list_filter = ('is_teacher', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('is_teacher',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('is_teacher',)}),
    )

class CohortMembershipInline(admin.TabularInline):
    model = CohortMembership
    extra = 1

class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'created_at')
    list_filter = ('teacher',)
    inlines = [CohortMembershipInline]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(CohortMembership)