# Generated by Django 2.2.11 on 2020-06-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_auto_20200621_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='enrollment_no',
            new_name='enroll',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='hostel_name',
            new_name='hostel',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='roll_no',
            new_name='roll',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='room',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
