from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    """
    A class representing the admin interface for the custom user model.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 
                    'first_name', 
                    'last_name', 
                    'email', 
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'department', 
                    'date_of_birth', 
)
    list_filter = ('is_active', 
                   'is_staff', 
                   'is_superuser', 
                   'department',)
    fieldsets = (
        (None, {'fields': ('username', 
                           'password', )}),
        ('Personal info', {'fields': ('first_name', 
                                      'middle_name',
                                      'last_name', 
                                      'email', 
                                      'department', 
                                      'date_of_birth',
                                      'faculty_id',)}),
        ('Permissions', {'fields': ('is_active', 
                                    'is_staff', 
                                    'is_superuser', )}),
        ('Important dates', {'fields': ('last_login', 
                                        'date_joined', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 
                       'first_name', 
                       'last_name', 
                       'email', 
                       'department', 
                       'date_of_birth', 
                       'date_of_employment', 
                       'is_active', 
                       'is_staff', 
                       'is_superuser', 
                       'password1', 
                       'password2', ),
        }),
    )
    search_fields = ('username', 
                     'first_name', 
                     'last_name', 
                     'email', 
                     'department',)
    
    
admin.site.register(CustomUser, CustomUserAdmin)

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
