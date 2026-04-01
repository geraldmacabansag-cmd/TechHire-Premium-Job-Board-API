from django.contrib import admin
from .models import JobPosting, UserProfile


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'salary_range', 'created_at')
    search_fields = ('title', 'company_name', 'description')
    list_filter = ('location',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership')
    list_filter = ('membership',)
    search_fields = ('user__username',)