# Generated by Django 5.1.6 on 2025-04-10 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('villa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignVilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('is_valid', models.BooleanField(default=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='villa.seller')),
            ],
        ),
    ]
