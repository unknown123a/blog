# Generated by Django 5.1.5 on 2025-01-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
