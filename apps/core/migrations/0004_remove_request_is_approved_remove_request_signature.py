# Generated by Django 5.2 on 2025-04-12 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_request_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='request',
            name='signature',
        ),
    ]
