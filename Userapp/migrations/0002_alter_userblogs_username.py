# Generated by Django 5.1.5 on 2025-01-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblogs',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
