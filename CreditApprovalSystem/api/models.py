from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Custome(User):
    customer_id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    approved_limit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    current_debt = models.DecimalField(max_digits=10, decimal_places=2)
