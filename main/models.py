from django.db import models
from django.db import models
from django.contrib.auth.models import User  # Assuming IMUser extends User


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=2000) 
    description = models.TextField(default='N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified= models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return super(self.name) 

class Cohort(models.Model):
    name = models.CharField(max_length=100)

class ClassSchedule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendee_attendances')
    is_present = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_attendances')

class Query(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_queries')
    resolution_status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved'),
    ], default='PENDING')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
