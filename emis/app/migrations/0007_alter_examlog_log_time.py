# Generated by Django 5.0.6 on 2024-07-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_examlog_log_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examlog',
            name='log_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
