from django.db import models


class Request(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, help_text="Enter a valid email address.")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    application = models.CharField(max_length=100)
    description = models.TextField()
    signature = models.TextField()
    is_approved = models.BooleanField(default=False)

    class Meta:
        db_table = "Request"
        verbose_name = "request"
        verbose_name_plural = "requests"
    
    def __str__(self):
        return self.application
