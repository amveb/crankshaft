# Generated by Django 3.0.4 on 2020-03-30 05:03

import contacts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20200329_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='contacts/photo', verbose_name='Фотография'),
        ),
    ]