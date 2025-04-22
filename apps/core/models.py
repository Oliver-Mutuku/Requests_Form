from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    application = models.CharField(max_length=200)
    description = models.TextField()
    signature = models.TextField()  # Store the signature data URL

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "request"
        verbose_name = "request"
        verbose_name_plural = "requests"

    def __str__(self):
        return self.application


class Approval(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='approvals')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True, null=True)
    signature = models.TextField()  # Admin signature data URL
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "approval"
        verbose_name = "approval"
        verbose_name_plural = "approvals"

    def __str__(self):
        return  self.request

