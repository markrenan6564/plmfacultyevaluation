
from django.db import models

class DocMajorComponent(models.Model):
    """
    A model representing a major component of a document.

    Attributes:
        docmajorcomponent_id (int): The primary key of the major component.
        docmajorcomponent_name (str): The name of the major component.
        docmajorcomponent_description (str): The description of the major component.
        is_active (bool): A flag indicating whether the major component is active or not.
    """
    docmajorcomponent_id = models.AutoField(primary_key=True)
    docmajorcomponent_name = models.CharField(max_length=255)
    docmajorcomponent_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.docmajorcomponent_name

class DocSubMajorComponent(models.Model):
    """
    A model representing a sub-major component of a document.

    Attributes:
        docsubmajorcomponent_id (int): The primary key of the sub-major component.
        docsubmajorcomponent_name (str): The name of the sub-major component.
        docsubmajorcomponent_description (str): The description of the sub-major component.
        is_active (bool): A flag indicating whether the sub-major component is active or not.
    """
    docsubmajorcomponent_id = models.AutoField(primary_key=True)
    docsubmajorcomponent_name = models.CharField(max_length=255)
    docsubmajorcomponent_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.docsubmajorcomponent_name
    
class DocSubMinorComponent(models.Model):
    """
    A model representing a sub-minor component of a document.

    Attributes:
        docsubminorcomponent_id (int): The primary key of the sub-minor component.
        docsubminorcomponent_name (str): The name of the sub-minor component.
        docsubminorcomponent_description (str): The description of the sub-minor component.
        is_active (bool): A flag indicating whether the sub-minor component is active or not.
    """
    docsubminorcomponent_id = models.AutoField(primary_key=True)
    docsubminorcomponent_name = models.CharField(max_length=255)
    docsubminorcomponent_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.docsubminorcomponent_name

class DocMinorComponent(models.Model):
    """
    A model representing a minor component of a document.

    Attributes:
        docminorcomponent_id (int): The primary key of the minor component.
        docminorcomponent_name (str): The name of the minor component.
        docminorcomponent_description (str): The description of the minor component.
        is_active (bool): A flag indicating whether the minor component is active or not.
    """
    docminorcomponent_id = models.AutoField(primary_key=True)
    docminorcomponent_name = models.CharField(max_length=255)
    docminorcomponent_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.docminorcomponent_name

class DocCategory(models.Model):
    """
    A model representing a category of a document.

    Attributes:
        doccategory_id (int): The primary key of the category.
        doccategory_name (str): The name of the category.
        doccategory_description (str): The description of the category.
        is_active (bool): A flag indicating whether the category is active or not.
    """
    doccategory_id = models.AutoField(primary_key=True)
    doccategory_name = models.CharField(max_length=255)
    doccategory_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.doccategory_name

class DocCriteria(models.Model):
    """
    A model representing a criteria of a document.

    Attributes:
        doccriteria_id (int): The primary key of the criteria.
        doccriteria_name (str): The name of the criteria.
        doccriteria_description (str): The description of the criteria.
        is_active (bool): A flag indicating whether the criteria is active or not.
    """
    doccriteria_id = models.AutoField(primary_key=True)
    doccriteria_name = models.CharField(max_length=255)
    doccriteria_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.doccriteria_name

class DocSubCriteria(models.Model):
    """
    A model representing a sub-criteria of a document.

    Attributes:
        docsubcriteria_id (int): The primary key of the sub-criteria.
        docsubcriteria_name (str): The name of the sub-criteria.
        docsubcriteria_description (str): The description of the sub-criteria.
        is_active (bool): A flag indicating whether the sub-criteria is active or not.
    """
    docsubcriteria_id = models.AutoField(primary_key=True)
    docsubcriteria_name = models.CharField(max_length=255)
    docsubcriteria_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.docsubcriteria_name

class Document(models.Model):
    """
    A model representing a document.

    Attributes:
        document_id (int): The primary key of the document.
        docmajor_id (int): The foreign key of the major component of the document.
        docsubmajor_id (int): The foreign key of the sub-major component of the document.
        docsubminor_id (int): The foreign key of the sub-minor component of the document.
        docminor_id (int): The foreign key of the minor component of the document.
        doccategory_id (int): The foreign key of the category of the document.
        doccriteria_id (int): The foreign key of the criteria of the document.
        docsubcriteria_id (int): The foreign key of the sub-criteria of the document.
        document_name (str): The name of the document.
        document_description (str): The description of the document.
        points (float): The points that support the document.
        max_points (float): The maximum points that the document can get.
        has_multiplier (bool): A flag indicating whether the document has a multiplier or not.
        multiplier_unit (str): The unit of the multiplier.
        is_active (bool): A flag indicating whether the document is active or not.
    """
    document_id = models.AutoField(primary_key=True)
    docmajor_id = models.ForeignKey('DocMajorComponent', on_delete=models.CASCADE)
    docsubmajor_id = models.ForeignKey('DocSubMajorComponent', on_delete=models.CASCADE, null=True)
    docsubminor_id = models.ForeignKey('DocSubMinorComponent', on_delete=models.CASCADE, null=True)
    docminor_id = models.ForeignKey('DocMinorComponent', on_delete=models.CASCADE, null=True)
    doccategory_id = models.ForeignKey('DocCategory', on_delete=models.CASCADE, null=True)
    doccriteria_id = models.ForeignKey('DocCriteria', on_delete=models.CASCADE, null=True)
    docsubcriteria_id = models.ForeignKey('DocSubCriteria', on_delete=models.CASCADE, null=True)
    document_name = models.CharField(max_length=255)
    document_description = models.TextField(null=True, blank=True)
    points = models.FloatField()
    max_points = models.FloatField()
    has_multiplier = models.BooleanField(default=False)
    multiplier_unit = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.document_name

