# Generated by Django 4.2.9 on 2024-02-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_date_created_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
