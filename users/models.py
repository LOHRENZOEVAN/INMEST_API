from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class IMUser(AbstractUser):
    USER_TYPES = [
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_permissions')
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')

class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohorts_created')

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='memberships')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_memberships')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohort_memberships')
