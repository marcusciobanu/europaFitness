# Generated by Django 4.2.8 on 2024-02-18 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_workout_time_started'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExerciseBank',
            new_name='Exercise',
        ),
    ]