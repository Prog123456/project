# Generated by Django 4.0.3 on 2024-05-23 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0004_breakin_clockin_delete_employeeaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in_time', models.DateTimeField(blank=True, null=True)),
                ('break_in_time', models.DateTimeField(blank=True, null=True)),
                ('break_out_time', models.DateTimeField(blank=True, null=True)),
                ('clock_out_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='clockin',
            name='user',
        ),
        migrations.DeleteModel(
            name='BreakIn',
        ),
        migrations.DeleteModel(
            name='ClockIn',
        ),
    ]
