# Generated by Django 2.2.6 on 2019-11-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_todoitem_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date',
            field=models.DateField(),
        ),
    ]
