# Generated by Django 2.0.2 on 2019-01-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20190117_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='mode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
