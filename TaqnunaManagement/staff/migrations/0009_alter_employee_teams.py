# Generated by Django 4.0.4 on 2022-05-01 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_employee_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='teams',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='staff.teams'),
        ),
    ]