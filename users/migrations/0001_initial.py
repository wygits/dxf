# Generated by Django 2.2.3 on 2019-07-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datadate', models.DateField(auto_created=True, auto_now_add=True)),
                ('sid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=10)),
            ],
        ),
    ]
