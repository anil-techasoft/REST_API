# Generated by Django 4.2 on 2023-04-18 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_remove_department_id_alter_department_department_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=20)),
                ('project_location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('ssn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('super_ssn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='EmployeeApp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_location', models.CharField(max_length=20)),
                ('department_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='manager_ssn',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.employee'),
        ),
        migrations.AddConstraint(
            model_name='departmentlocation',
            constraint=models.UniqueConstraint(fields=('department_no', 'department_location'), name='unique_migration_host_combination'),
        ),
    ]
