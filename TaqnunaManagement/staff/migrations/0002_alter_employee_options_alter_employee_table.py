# Generated by Django 4.0.4 on 2022-04-30 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': True, 'verbose_name': 'ModelName', 'verbose_name_plural': 'ModelNames'},
        ),
        migrations.AlterModelTable(
            name='employee',
            table='',
        ),
    ]