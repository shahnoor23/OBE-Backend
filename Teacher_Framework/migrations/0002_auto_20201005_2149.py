# Generated by Django 2.2.13 on 2020-10-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chairman_Framework', '0001_initial'),
        ('Teacher_Framework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(to='Chairman_Framework.CLO'),
        ),
    ]