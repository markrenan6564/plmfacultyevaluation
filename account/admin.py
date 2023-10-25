from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class UserAdminConfig(UserAdmin):
    
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_added',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'plm_email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    
admin.site.register(Account, UserAdminConfig)

admin.site.register(Department)
admin.site.register(College)
admin.site.register(CollegeReviewRankingCommitteeRole)
admin.site.register(CollegeReviewRankingCommittee)
admin.site.register(Rank)
admin.site.register(SubRank)
admin.site.register(SalaryGrade)
admin.site.register(FacultyRank)
admin.site.register(EmploymentStatus)
admin.site.register(HiringNature)
# END: 6hj8d9f3k4s2
