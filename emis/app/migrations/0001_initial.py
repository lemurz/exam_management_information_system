# Generated by Django 5.0.6 on 2024-07-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=100)),
                ('student_count', models.CharField(max_length=100)),
                ('additional_details', models.CharField(max_length=100)),
            ],
        ),
    ]