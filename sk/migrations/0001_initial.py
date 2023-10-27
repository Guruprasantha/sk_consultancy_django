# Generated by Django 4.2.6 on 2023-10-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('d_no', models.CharField(max_length=20)),
                ('s_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=100)),
                ('mobile_no2', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=100)),
                ('issue', models.CharField(max_length=100)),
            ],
        ),
    ]
