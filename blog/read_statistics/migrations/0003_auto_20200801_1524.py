# Generated by Django 3.0.8 on 2020-08-01 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0002_readdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readdetail',
            old_name='objects_id',
            new_name='object_id',
        ),
    ]
