# Generated by Django 2.2.11 on 2020-06-22 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='room_no',
            new_name='room',
        ),
    ]
