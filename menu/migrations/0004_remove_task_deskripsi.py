# Generated by Django 4.2.6 on 2023-12-29 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_task_status_alter_task_tanggal_jatuh_tempo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deskripsi',
        ),
    ]
