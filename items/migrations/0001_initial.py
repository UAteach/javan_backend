# Generated by Django 3.1 on 2020-08-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('MATH', 'Mathematics'), ('CHEM', 'Chemistry'), ('BIO', 'Biology'), ('HOUSE', 'Household'), ('CRAFT', 'Craft'), ('PHYS', 'Physics'), ('TOY', 'Toy'), ('TECH', 'Tech')], max_length=5)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
