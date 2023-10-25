from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    """
    A model representing a department in the university.

    Attributes:
        department_id (int): The unique identifier of the department.
        department_name (str): The name of the department.
        department_description (str): A brief description of the department.
        is_active (bool): A flag indicating whether the department is active or not.
    """
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
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
        college_description (str): The description of the college.
        is_active (bool): A flag indicating whether the college is active or not.
    """
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=100)
    college_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.college_name

class CustomUser(AbstractUser):
    """
    A model representing a custom user.

    Attributes:
        department_id (int): The foreign key referencing the Department model.
        college_id (int): The foreign key referencing the College model.
        middle_name (str): The middle name of the user.
        faculty_id (str): The faculty ID of the user.
        birthdate (date): The birthdate of the user.
        plm_email (str): The PLM email of the user.
        contact_no (str): The contact number of the user.
        address (str): The address of the user.
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    faculty_id = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    plm_email = models.EmailField(max_length=254, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.email}:{self.first_name} {self.last_name}'


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
        user_id (int): The foreign key referencing the CustomUser model.
        role_id (int): The foreign key referencing the CollegeReviewRankingCommitteeRole model.
        department_id (int): The foreign key referencing the Department model.
        college_id (int): The foreign key referencing the College model.
        date_modified (datetime): The date when the committee was last modified.
        has_credentials (bool): A flag indicating whether the user has permission to access the admin dashboard.
        is_active (bool): A flag indicating whether the committee is active or not.
    """
    crrc_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role_id = models.ForeignKey(CollegeReviewRankingCommitteeRole, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
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
        rank_id (int): The foreign key referencing the Rank model.
        subrank_id (int): The foreign key referencing the SubRank model.
        salarygrade_id (int): The foreign key referencing the SalaryGrade model.
        facultyrank_description (str): A brief description of the faculty rank.
        minpoints (int): The minimum points required for the faculty rank.
        maxpoints (int): The maximum points required for the faculty rank.
        is_active (bool): A flag indicating whether the faculty rank is active or not.
    """
    facultyrank_id = models.AutoField(primary_key=True)
    rank_id = models.ForeignKey(Rank, on_delete=models.CASCADE)
    subrank_id = models.ForeignKey(SubRank, on_delete=models.CASCADE, null=True)
    salarygrade_id = models.ForeignKey(SalaryGrade, on_delete=models.CASCADE)
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

