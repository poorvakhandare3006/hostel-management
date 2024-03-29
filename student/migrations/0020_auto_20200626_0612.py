# Generated by Django 2.2.13 on 2020-06-26 06:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_auto_20200625_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='name', max_length=50)),
                ('student_email', models.EmailField(default='pk@pk.com', max_length=254)),
                ('hostel', models.CharField(max_length=3, null=True)),
                ('room_c', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=10, null=True)),
                ('date_out', models.DateField()),
                ('date_in', models.DateField()),
                ('reason', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=3000)),
                ('s_contact', models.CharField(max_length=9999999999)),
                ('p_contact', models.CharField(max_length=9999999999)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='student_email',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='p_contact',
        ),
        migrations.AddField(
            model_name='complaint',
            name='student_name',
            field=models.CharField(default='name', max_length=254),
        ),
        migrations.AddField(
            model_name='gatepass',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
