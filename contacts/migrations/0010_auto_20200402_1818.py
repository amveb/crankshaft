# Generated by Django 3.0.4 on 2020-04-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='ok_social',
        ),
        migrations.AddField(
            model_name='contact',
            name='inst_social',
            field=models.URLField(blank=True, verbose_name='Ссылка Инстграмм'),
        ),
    ]