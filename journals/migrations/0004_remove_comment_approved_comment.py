# Generated by Django 2.2.2 on 2019-12-13 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
