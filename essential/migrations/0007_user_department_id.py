# Generated by Django 5.0.2 on 2024-04-26 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential', '0006_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='essential.department'),
        ),
    ]