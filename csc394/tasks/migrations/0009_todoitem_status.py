# Generated by Django 2.2.6 on 2019-11-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_remove_todoitem_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.TextField(default='inProgress'),
        ),
    ]
