# Generated by Django 3.1.2 on 2020-10-08 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20201008_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='projects',
            new_name='project',
        ),
    ]