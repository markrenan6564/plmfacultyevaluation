from django.db import models

from account.models import Account
from document.models import Document

from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
class Evaluation(models.Model):
    evaluation_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    
    details = models.JSONField()
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.document.title + " - " + self.evaluator.email