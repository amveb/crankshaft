# Generated by Django 3.0.4 on 2020-03-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20200330_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='contacts/photo', verbose_name='Фотография'),
        ),
    ]