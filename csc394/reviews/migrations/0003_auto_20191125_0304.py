# Generated by Django 2.2.6 on 2019-11-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20191124_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='additionalInfo',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='improvement',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='performance',
            field=models.TextField(max_length=100),
        ),
    ]
