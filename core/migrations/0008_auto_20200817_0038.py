# Generated by Django 3.1 on 2020-08-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200812_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Mentor'), (0, 'Student'), (2, 'Work Study'), (4, 'Admin'), (3, 'Master Teacher')], default=0),
        ),
    ]
