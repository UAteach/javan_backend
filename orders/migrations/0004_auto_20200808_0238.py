# Generated by Django 3.1 on 2020-08-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200808_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'STARTED'), (0, 'ASSIGNED'), (8, 'EMPTIED'), (5, 'SELF-FILLED'), (2, 'PLACED'), (4, 'FILLED'), (3, 'UPDATED'), (7, 'RETURNED'), (9, 'DONE'), (6, 'OUT')], default=0),
        ),
    ]
