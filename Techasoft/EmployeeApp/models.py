from django.db import models


# Create your models here.
class Employee(models.Model):
    ssn = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    super_ssn = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subordinates')


class Department(models.Model):
    department_no = models.CharField(max_length=20, primary_key=True)
    department_name = models.CharField(max_length=20)
    manager_ssn = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)


class DepartmentLocation(models.Model):
    department_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    department_location = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['department_no', 'department_location'], name='unique_migration_host_combination'
            )
        ]


class Project(models.Model):
    project_no = models.CharField(max_length=20, primary_key=True)
    project_name = models.CharField(max_length=20)
    project_location = models.CharField(max_length=20)
    department_no = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
