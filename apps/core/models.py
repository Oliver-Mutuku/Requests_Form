from django.db import models
from django.utils import timezone

class Request(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, help_text="Enter a valid email address.")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    application = models.CharField(max_length=100)
    description = models.TextField()
    signature = models.TextField()
    date_of_request = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "request"
        verbose_name = "request"
        verbose_name_plural = "requests"
    
    def __str__(self):
        return self.application

class Approval(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    signature = models.TextField()
    description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "approval"
        verbose_name = "approval"
        verbose_name_plural = "approvals"

    def __str__(self):
        return  self.request
