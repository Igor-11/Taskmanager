# Generated by Django 3.2.6 on 2021-09-15 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynewapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='copy_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mynewapp.task'),
        ),
    ]
