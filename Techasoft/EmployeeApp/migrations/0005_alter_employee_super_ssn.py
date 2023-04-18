# Generated by Django 4.2 on 2023-04-18 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0004_project_department_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='super_ssn',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='EmployeeApp.employee'),
        ),
    ]