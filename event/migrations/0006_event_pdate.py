# Generated by Django 2.0.2 on 2019-01-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_remove_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pdate',
            field=models.DateTimeField(null=True),
        ),
    ]
