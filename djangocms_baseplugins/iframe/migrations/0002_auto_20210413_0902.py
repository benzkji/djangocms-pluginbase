# Generated by Django 2.2.20 on 2021-04-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iframe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iframe',
            name='iframe_url',
            field=models.CharField(default='', max_length=1024, verbose_name='URL'),
        ),
    ]
