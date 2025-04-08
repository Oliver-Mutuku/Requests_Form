from django.db import models


class Request(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, help_text="Enter a valid email address.")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()
    signature = models.TextField()




