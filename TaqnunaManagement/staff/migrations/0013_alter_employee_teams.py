# Generated by Django 4.0.4 on 2022-05-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_alter_employee_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='teams',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
