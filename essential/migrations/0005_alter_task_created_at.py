# Generated by Django 5.0.2 on 2024-04-24 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential', '0004_alter_issue_created_at_alter_project_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
