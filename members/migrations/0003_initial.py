# Generated by Django 4.0.3 on 2024-05-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in_updated', models.DateTimeField(auto_now=True)),
                ('clock_in_created', models.DateTimeField(auto_now_add=True)),
                ('break_in_updated', models.DateTimeField(auto_now=True)),
                ('break_in_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]