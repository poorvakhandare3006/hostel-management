
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20200620_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),

                ('room_no', models.CharField(max_length=10)),

                ('category', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(help_text="what's the issue ...")),
            ],
        ),
    ]
