from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import AccountManager

from django.conf import settings
from django.contrib.auth import get_user_model

class Department(models.Model):
    """
    A model representing a department in the university.

    Attributes:
        department_id (int): The unique identifier of the department.
        department_name (str): The name of the department.
        department_abbreviation (str): The abbreviation of the department.
        department_description (str): A brief description of the department.
        is_active (bool): A flag indicating whether the department is active or not.
    """
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    department_abbreviation = models.CharField(max_length=100)
    department_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.department_name

class College(models.Model):
    """
    A model representing a college.

    Attributes:
        college_id (int): The primary key of the college.
        college_name (str): The name of the college.
        college_abbreviation (str): The abbreviation of the college.
        college_description (str): The description of the college.
        is_active (bool): A flag indicating whether the college is active or not.
    """
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=100)
    college_abbreviation = models.CharField(max_length=100)
    college_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.college_name

class CollegeReviewRankingCommitteeRole(models.Model):
    """
    A model representing a role in the college review ranking committee.

    Attributes:
        role_id (int): The unique identifier of the role.
        role_name (str): The name of the role.
        role_description (str): A brief description of the role.
        is_active (bool): A flag indicating whether the role is active or not.
    """
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    role_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.role_name

class CollegeReviewRankingCommittee(models.Model):
    """
    A model representing a college review ranking committee.

    Attributes:
        crrc_id (int): The unique identifier of the committee.
        account (int): The foreign key referencing the CustomUser model.
        role (int): The foreign key referencing the CollegeReviewRankingCommitteeRole model.
        department_id (int): The foreign key referencing the Department model.
        college_id (int): The foreign key referencing the College model.
        date_modified (datetime): The date when the committee was last modified.
        has_credentials (bool): A flag indicating whether the user has permission to access the admin dashboard.
        is_active (bool): A flag indicating whether the committee is active or not.
    """
    crrc_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(CollegeReviewRankingCommitteeRole, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    has_credentials = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.committee_name
    
class Rank(models.Model):
    """
    A model representing a rank in the university.

    Attributes:
        rank_id (int): The unique identifier of the rank.
        rank_name (str): The name of the rank.
        rank_description (str): A brief description of the rank.
        is_active (bool): A flag indicating whether the rank is active or not.
    """
    rank_id = models.AutoField(primary_key=True)
    rank_name = models.CharField(max_length=100)
    rank_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.rank_name


class SubRank(models.Model):
    """
    A model representing a subrank in the university.

    Attributes:
        subrank_id (int): The unique identifier of the subrank.
        subrank_tier (str): The tier of the subrank.
        subrank_description (str): A brief description of the subrank.
        is_active (bool): A flag indicating whether the subrank is active or not.
    """
    subrank_id = models.AutoField(primary_key=True)
    subrank_tier = models.CharField(max_length=100)
    subrank_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subrank_description

class SalaryGrade(models.Model):
    """
    A model representing a salary grade in the university.

    Attributes:
        salarygrade_id (int): The unique identifier of the salary grade.
        salarygrade_tier (str): The tier of the salary grade.
        salarygrade_description (str): A brief description of the salary grade.
        salary_grade_value (Decimal): The value of the salary grade in currency.
        is_active (bool): A flag indicating whether the salary grade is active or not.
    """
    salarygrade_id = models.AutoField(primary_key=True)
    salarygrade_tier = models.CharField(max_length=100)
    salarygrade_description = models.TextField(null=True, blank=True)
    salary_grade_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.salarygrade_tier

class FacultyRank(models.Model):
    """
    A model representing a faculty rank in the university.

    Attributes:
        facultyrank_id (int): The unique identifier of the faculty rank.
        rank (int): The foreign key referencing the Rank model.
        subrank (int): The foreign key referencing the SubRank model.
        salarygrade (int): The foreign key referencing the SalaryGrade model.
        facultyrank_description (str): A brief description of the faculty rank.
        minpoints (int): The minimum points required for the faculty rank.
        maxpoints (int): The maximum points required for the faculty rank.
        is_active (bool): A flag indicating whether the faculty rank is active or not.
    """
    facultyrank_id = models.AutoField(primary_key=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    subrank = models.ForeignKey(SubRank, on_delete=models.CASCADE, null=True)
    salarygrade = models.ForeignKey(SalaryGrade, on_delete=models.CASCADE)
    facultyrank_description = models.TextField(null=True, blank=True)
    minpoints = models.IntegerField()
    maxpoints = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.facultyrank_description

class EmploymentStatus(models.Model):
    """
    A model representing an employment status in the university.

    Attributes:
        empstatus_id (int): The unique identifier of the employment status.
        empstatus_name (str): The title of the employment status.
        empstatus_description (str): A brief description of the employment status.
        is_active (bool): A flag indicating whether the employment status is active or not.
    """
    empstatus_id = models.AutoField(primary_key=True)
    empstatus_name = models.CharField(max_length=100)
    empstatus_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.empstatus_title

class HiringNature(models.Model):
    """
    A model representing a hiring nature in the university.

    Attributes:
        hiringnature_id (int): The unique identifier of the hiring nature.
        hiringnature_name (str): The name of the hiring nature.
        hiringnature_description (str): A brief description of the hiring nature.
        is_active (bool): A flag indicating whether the hiring nature is active or not.
    """
    hiringnature_id = models.AutoField(primary_key=True)
    hiringnature_name = models.CharField(max_length=100)
    hiringnature_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.hiringnature_name

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')
        account = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_staff = True
        account.is_superuser = True
        account.save()
        return account

class FacultyRankHistory(models.Model):
    """
    Model representing the history of faculty rank changes.

    Fields:
    - accountrankhistory_id: AutoField, primary key
    - user: ForeignKey to AUTH_USER_MODEL, on_delete CASCADE
    - currentrank: ForeignKey to FacultyRank, related name 'current_rank', on_delete CASCADE
    - currentnature: ForeignKey to HiringNature, related name 'current_nature', on_delete CASCADE
    - currentstatus: ForeignKey to EmploymentStatus, related name 'current_status', on_delete CASCADE
    - targetrank: ForeignKey to FacultyRank, related name 'target_rank', on_delete CASCADE
    - targetnature: ForeignKey to HiringNature, related name 'target_nature', on_delete CASCADE
    - targetstatus: ForeignKey to EmploymentStatus, related name 'target_status', on_delete CASCADE
    - date_of_request: DateTimeField, default timezone.now
    - is_successful: BooleanField, default False
    - date_of_promotion: DateTimeField, blank and null allowed
    - is_active: BooleanField, default True
    """
    accountrankhistory_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    currentrank = models.ForeignKey(FacultyRank, on_delete=models.CASCADE, related_name='current_rank', blank=True, null=True)
    currentnature = models.ForeignKey(HiringNature, on_delete=models.CASCADE, related_name='current_nature', blank=True, null=True)
    currentstatus = models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE, related_name='current_status', blank=True, null=True)
    
    targetrank = models.ForeignKey(FacultyRank, on_delete=models.CASCADE, related_name='target_rank', blank=True, null=True)
    targetnature = models.ForeignKey(HiringNature, on_delete=models.CASCADE, related_name='target_nature', blank=True, null=True)
    targetstatus = models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE, related_name='target_status', blank=True, null=True)
    
    date_of_request = models.DateTimeField(default=timezone.now)
    is_successful = models.BooleanField(default=False)
    date_of_promotion = models.DateTimeField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)


class Account(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for PLM Faculty Evaluation app.

    Fields:
    - email: EmailField, max_length=100, unique=True
    - first_name: CharField, max_length=100, default=''
    - middle_name: CharField, max_length=100, blank=True, default=''
    - last_name: CharField, max_length=100, default=''
    - faculty_id: CharField, max_length=100, blank=True, default=''
    - plm_email: EmailField, max_length=100, blank=True, default=''
    - college: ForeignKey to College model, on_delete=models.CASCADE, null=True
    - department: ForeignKey to Department model, on_delete=models.CASCADE, null=True
    - date_of_birth: DateField, null=True, blank=True
    - contact_number: CharField, max_length=100, blank=True, default=''
    - address: TextField, blank=True, default=''
    - date_added: DateTimeField, default=timezone.now
    - is_staff: BooleanField, default=False
    - is_active: BooleanField, default=True

    Methods:
    - __str__: Returns the full name of the user.
    - get_full_name: Returns the full name and email of the user.
    - get_short_name: Returns the first name of the user.
    """
    
    email = models.EmailField(max_length=100, unique=True)
    
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, default='')
    
    faculty_id = models.CharField(max_length=100, blank=True, default='')
    plm_email = models.EmailField(max_length=100, blank=True, default='')
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    
    date_of_birth = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=100, blank=True, default='')
    address = models.TextField(blank=True, default='')
    
    currentrank = models.ForeignKey(FacultyRankHistory, on_delete=models.CASCADE, related_name='current_rank', blank=True, null=True)
    
    date_added = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self) -> str:   
        return f'{self.first_name} {self.last_name}'
    
    def get_full_name(self):
        """
        Returns the full name and email of the user.
        """
        return f'{self.email}: {self.first_name} {self.last_name}'
    
    def get_short_name(self):
        """
        Returns the first name of the user.
        """
        return self.first_name
    

