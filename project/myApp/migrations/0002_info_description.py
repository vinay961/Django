# Generated by Django 5.0.6 on 2024-06-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
