# Generated by Django 2.2.3 on 2019-07-23 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='users',
        ),
    ]