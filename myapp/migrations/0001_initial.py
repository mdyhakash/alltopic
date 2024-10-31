# Generated by Django 5.1.2 on 2024-10-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_title', models.CharField(max_length=200)),
                ('c_code', models.CharField(max_length=20)),
                ('c_teacher', models.CharField(max_length=100)),
                ('s_mid', models.TextField()),
                ('s_final', models.TextField()),
                ('c_description', models.TextField()),
                ('c_link', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
