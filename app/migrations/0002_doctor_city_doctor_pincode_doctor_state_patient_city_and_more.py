# Generated by Django 5.0.3 on 2024-06-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='pincode',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='doctor',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='pincode',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
    ]
