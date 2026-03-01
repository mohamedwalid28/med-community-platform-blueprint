from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Oncologist'),
        ('MODERATOR', 'Staff'),
        ('MEMBER', 'Patient'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    is_premium = models.BooleanField(default=False)