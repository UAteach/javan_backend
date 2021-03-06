# Generated by Django 3.1 on 2020-08-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200812_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('UPDATED', 'UPDATED'), ('STARTED', 'STARTED'), ('SELF-FILLED', 'SELF-FILLED'), ('EMPTIED', 'EMPTIED'), ('DONE', 'DONE'), ('FILLED', 'FILLED'), ('RETURNED', 'RETURNED'), ('OUT', 'OUT'), ('ASSIGNED', 'ASSIGNED'), ('PLACED', 'PLACED')], default='ASSIGNED', max_length=11),
        ),
    ]
