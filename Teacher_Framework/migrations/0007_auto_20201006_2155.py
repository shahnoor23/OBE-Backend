# Generated by Django 2.2.13 on 2020-10-06 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher_Framework', '0006_auto_20201006_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graded_questions',
            old_name='graded',
            new_name='graded_assignment',
        ),
    ]
