# Generated by Django 5.1.5 on 2025-01-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountsapp', '0003_alter_logintable_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.BooleanField(default='True', null=True),
        ),
    ]
