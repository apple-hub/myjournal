# Generated by Django 2.2.2 on 2019-12-10 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='journal',
            name='updated_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
