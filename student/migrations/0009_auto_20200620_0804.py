# Generated by Django 2.2.11 on 2020-06-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200620_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatepass',
            name='id',
        ),
        migrations.AddField(
            model_name='gatepass',
            name='gatepass_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
