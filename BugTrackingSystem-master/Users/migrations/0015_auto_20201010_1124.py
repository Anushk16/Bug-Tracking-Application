# Generated by Django 3.1.2 on 2020-10-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_auto_20201010_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
