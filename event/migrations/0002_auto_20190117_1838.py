# Generated by Django 2.0.2 on 2019-01-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='event',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]