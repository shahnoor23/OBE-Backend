# Generated by Django 2.2.13 on 2020-10-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20201006_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='batch',
            field=models.CharField(default=False, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(default=False, max_length=255, null=True),
        ),
    ]