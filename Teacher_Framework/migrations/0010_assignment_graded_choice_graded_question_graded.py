# Generated by Django 2.2.13 on 2020-10-06 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Teacher_Framework', '0009_auto_20201007_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Graded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice_Graded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher_Framework.Question_Graded')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment_Graded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_cr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
