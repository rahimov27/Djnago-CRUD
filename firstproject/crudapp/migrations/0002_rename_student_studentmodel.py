# Generated by Django 4.2.6 on 2023-10-17 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentModel',
        ),
    ]