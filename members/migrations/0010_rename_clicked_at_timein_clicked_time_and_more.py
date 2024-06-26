# Generated by Django 4.0.3 on 2024-05-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_timein_clicked_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timein',
            old_name='clicked_at',
            new_name='clicked_time',
        ),
        migrations.RemoveField(
            model_name='lunchin',
            name='clicked_at',
        ),
        migrations.RemoveField(
            model_name='lunchout',
            name='clicked_at',
        ),
        migrations.RemoveField(
            model_name='timeout',
            name='clicked_at',
        ),
        migrations.AddField(
            model_name='lunchin',
            name='clicked_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='lunchin',
            name='clicked_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='lunchout',
            name='clicked_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='lunchout',
            name='clicked_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='timein',
            name='clicked_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='timeout',
            name='clicked_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='timeout',
            name='clicked_time',
            field=models.TimeField(null=True),
        ),
    ]
