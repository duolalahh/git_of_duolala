# Generated by Django 2.0 on 2020-11-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='', upload_to='photo', verbose_name='头像'),
        ),
    ]
