# Generated by Django 2.2.13 on 2020-06-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20200629_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Disable', 'Disable'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Disable', 'Disable'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Disable', 'Disable'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Active', max_length=10),
        ),
    ]
