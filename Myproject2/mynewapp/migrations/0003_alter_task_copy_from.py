# Generated by Django 3.2.6 on 2021-09-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynewapp', '0002_task_copy_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='copy_from',
            field=models.ForeignKey(db_column='copy_from', null=True, on_delete=django.db.models.deletion.CASCADE, to='mynewapp.task'),
        ),
    ]
